import os
import yaml
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
import ast
from crewai import Crew
from testing_crew.crew import TestingCrew

load_dotenv()

# Disable CrewAI telemetry only
os.environ['CREWAI_DISABLE_TELEMETRY'] = 'true'

# Disable all OpenTelemetry (including CrewAI)
os.environ['OTEL_SDK_DISABLED'] = 'true'

def load_config(filepath="src/testing_crew/config/config.yaml"):
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)

# def fetch_data(company_name):
#     try:
#         tool = SerperDevTool(
#             country="in",
#             locale="en-IN",
#             location="Mumbai, Maharashtra, India",
#             n_results=3,
#         )

#         results = tool.run(search_query=company_name)
#         return results

#     except Exception as e:
#         print(f"Error fetching data from SerpAPI: {e}")
#         return None
    
# def parse_data(data):
#     # query = data['searchParameters']['q']
#     # location = data['searchParameters']['location']
#     top_results = data['organic']
#     # related_searches = [item['query'] for item in data['relatedSearches']]
#     # credits_used = data['credits'] 
    
#     return top_results  


def main():
    config = load_config()
    company_name = config['company_name']
    
    crew = TestingCrew()
    my_crew = crew.crew()

    # my_crew.plot("flowPlot")
    my_crew.kickoff(inputs={'topic': company_name})
    
if __name__ == "__main__":
    main()
