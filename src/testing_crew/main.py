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

# Load environment variables
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
        return results  # Now returning the results

    except Exception as e:
        print(f"Error fetching data from SerpAPI: {e}")
        return None
    
def parse_data(data):
    query = data['searchParameters']['q']
    location = data['searchParameters']['location']
    top_results = data['organic']
    related_searches = [item['query'] for item in data['relatedSearches']]
    credits_used = data['credits'] 
    
    return top_results  

def analyze_data(data, reporting_analyst):
    print("Data Analysis:")
    analysis_result = reporting_analyst.run(data=data)
    print("Analysis Result:", analysis_result)
    return analysis_result

def generate_brand_summary(company_name, analysis_result):
    summary = f"Brand Summary for {company_name}:\n"
    summary += f"{analysis_result}\n"
    summary += "--- End of Summary ---"
    return summary

def main():
    config = load_config()
    company_name = config['company_name']

    # Initialize the crew
    crew = TestingCrew()
    my_crew = crew.crew()

    researcher = my_crew.agents[0]
    reporting_analyst = my_crew.agents[1]
    
    data = fetch_data(company_name)

    if data:
        print(data)
        parsed_data = parse_data(data)
        
        analysis_result = analyze_data(parsed_data, reporting_analyst)
        
        brand_summary = generate_brand_summary(company_name, analysis_result)
        print(brand_summary)

        df = pd.DataFrame([{'Company Name': company_name, 'Brand Summary': brand_summary}])
        csv_filepath = 'brand_summary.csv'
        file_exists = os.path.isfile(csv_filepath)

        df.to_csv(csv_filepath, mode='a', header=not file_exists, index=False)
        print(f"Brand summary appended to {csv_filepath}")
    else:
        print("Failed to retrieve data.")

if __name__ == "__main__":
    main()
