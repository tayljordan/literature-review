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

-Queries multiple search engines (Google Scholar, arXiv, CrossRef).
-Filters the results based on defined keywords.
-Prepares a prompt for the OpenAI model to generate a literature review.
-Outputs a one-paragraph literature review with a quantitative research gap rating, in APA format.

## Example Output #1

Result:  [RESEARCH GAP: 10] Current literature and available databases, including Google Scholar, arXiv, and CrossRef, show a significant absence of studies on Python imaging tools or models specifically designed for analyzing marine engineering drawings. This gap is evident given the absence of search results on arXiv, where a query returned no matching results (arXiv, 2024). Despite Python's prevalent use in image processing and its potential applications in engineering disciplines due to libraries like OpenCV and PIL, there appears to be a critical lack of targeted research integrating these tools with marine engineering needs. This lack of literature underscores a pressing opportunity for focused investigations and technological development in this intersectional field of study, which remains unaddressed in current academic discourse.

## License

This project is licensed under the MIT License. 

