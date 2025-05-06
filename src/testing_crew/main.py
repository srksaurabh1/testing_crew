import os
import yaml
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
# from serpapi import GoogleSearch
from crewai_tools import SerperDevTool

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


def analyze_data(data):
    print("Data Analysis:")
    for i, item in enumerate(data[:3], 1):  # Top 3 results
        print(f"{i}. {item.get('title')}: {item.get('link')}")
    return "Top search results analyzed"

def generate_brand_summary(company_name, analysis_result):
    summary = f"Brand Summary for {company_name}:\n"
    summary += f"{analysis_result}\n"
    summary += "--- End of Summary ---"
    return summary

def main():
    config = load_config()
    company_name = config['company_name']

    data = fetch_data(company_name)
    

    if data:
        print(data)
        analysis_result = analyze_data(data)
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
