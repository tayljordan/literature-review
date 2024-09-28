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

