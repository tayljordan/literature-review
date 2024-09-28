# Scholarly Search and Literature Review Automation

This repository contains a Python script that integrates multiple scholarly search engines (Google Scholar, arXiv, and CrossRef) with the OpenAI API to automate the generation of literature reviews. The script is designed to perform a combined search across these platforms and summarize the results into a concise scientific literature review, rated with a research gap score.

## Requirements

- Python 3.11
- Dependencies listed in `requirements.txt`

## Dependencies

- `tqdm~=4.66.5`: For the progress bar.
- `python-dotenv~=1.0.1`: To load environment variables from a configuration file.
- `requests~=2.32.3`: To handle HTTP requests.
- `scholarly~=1.7.11`: For searching Google Scholar.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/repository.git
    cd repository
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables in a `config.txt` file:

    ```txt
    OPENAI_API_KEY=your_openai_api_key
    OPENAI_MODEL=your_openai_model
    ```

## Usage

The main execution script `literature_review.py` can be run with the following command:

```bash
python3.11 literature_review.py
```
## Example Subject Matter

The script allows you to define subject matter and specific keywords to narrow down the search results. For example:

```python
proposed_subject_matter = """
    What is the best python imaging tool and/or model to use for examining marine engineering drawings?
"""
must_contain = ["maritime"]
```
## Output

The script performs the following:

- Queries multiple search engines (Google Scholar, arXiv, CrossRef).
- Filters the results based on defined keywords.
- Prepares a prompt for the OpenAI model to generate a literature review.
- Outputs a one-paragraph literature review with a quantitative research gap rating, in APA format.

## Example Output #1

Result:  [RESEARCH GAP: 10] The inquiry into the optimal Python imaging tool or model for analyzing marine engineering drawings yields no substantial results across major academic databases, indicating a significant research gap. Searches conducted in Google Scholar, arXiv, and CrossRef returned no relevant publications or studies addressing this specific intersection of software tool development and application in marine engineering contexts. The absence of literature suggests an unexplored intersection of computer science, particularly Python's capabilities in image processing, with the practical requirements of marine engineering (arXiv, 2024). This lack of existing research highlights an opportunity for pioneering studies that could develop bespoke solutions or adapt existing image processing frameworks for the nuanced requirements of interpreting technical drawings in this field.

## License

This project is licensed under the MIT License. 

