import os
import yaml
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
# from serpapi import GoogleSearch
from crewai_tools import SerperDevTool
import ast
from crewai import Crew
from testing_crew.crew import TestingCrew

load_dotenv()

def load_config(filepath="src/testing_crew/config/config.yaml"):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

def fetch_data(company_name):
    try:
        tool = SerperDevTool(
            country="in",
            locale="en-IN",
            location="Mumbai, Maharashtra, India",
            n_results=3,
        )

        results = tool.run(search_query=company_name)
        return results

    except Exception as e:
        print(f"Error fetching data from SerpAPI: {e}")
        return None
    
def parse_data(data):
    # query = data['searchParameters']['q']
    # location = data['searchParameters']['location']
    top_results = data['organic']
    # related_searches = [item['query'] for item in data['relatedSearches']]
    # credits_used = data['credits'] 
    
    return top_results  

def main():
    config = load_config()
    company_name = config['company_name']

    data = fetch_data(company_name)
    
    if data:
        parsed_data = parse_data(data)
    
    crew = TestingCrew()
    my_crew = crew.crew()

    # researcher        = my_crew.agents[0]
    # reporting_analyst = my_crew.agents[1]
    
    my_crew.kickoff(inputs={'topic': company_name})
    
if __name__ == "__main__":
    main()
