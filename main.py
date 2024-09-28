#!/usr/bin/env python3.11
from api_calls.language_model import open_ai
from search_engines.scholarly_search import combined_search
from tqdm import tqdm
from dotenv import load_dotenv
import os

# Load environment variables
root_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(root_path, 'config.txt')
load_dotenv(config_path)
openai_model = os.getenv('OPENAI_MODEL')

if not openai_model:
    raise ValueError("OpenAI model not found. Check your config file.")

def main(subject_matter, contains):
    """Main execution function."""
    print("Running query through scholarly, arXiv, CrossRef search...")

    # Run search with a progress bar
    for _ in tqdm(range(10)):  # Removed colour argument for compatibility
        search_results = combined_search(subject_matter, contains)

    # Prepare the prompt for OpenAI API
    prompt_template = f"""
    Write a literature review based on the following {search_results}.
    Output must be one paragraph with inline citations.
    APA format.
    Use style of hard scientific literature review i.e. concise and to-the-point.
    Do not use adjectives under any circumstances.
    At the beginning, quantitatively rate research gap in bracket + ALL CAPS 1-10 
    where 1 is no research gap and 10 is large research gap. Example output: [RESEARCH GAP: 7]
    """

    # Call the OpenAI model
    lm_final_results = open_ai(prompt_template, openai_model=openai_model)
    print('Result: ', lm_final_results)

if __name__ == "__main__":
    # Define search parameters
    proposed_subject_matter = """
        What is the best python imaging tool and/or model to use for examining marine engineering drawings?
    """
    must_contain = ["maritime"]

    # Run the main function
    main(proposed_subject_matter, must_contain)
