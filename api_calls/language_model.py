from functools import wraps
import logging
import os
import requests
from dotenv import load_dotenv

root_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(root_path, '../config.txt')  # No leading '/'
load_dotenv(config_path)
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    os.environ['OPENAI_API_KEY'] = openai_api_key
else:
    raise ValueError("OpenAI API key not found. Check your config file.")

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {str(e)}")
            return {"error": f"{func.__name__} failed. Try another way."}

    return wrapper

@error_handler
def open_ai(query: str, openai_model: str):
    # Get API key from environment variables
    api_key = os.environ.get('OPENAI_API_KEY')

    if not api_key:
        raise ValueError("OpenAI API key not found in environment variables.")

    api_endpoint = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    payload = {
        "model": openai_model,
        "messages": [{"role": "user", "content": query}],
    }

    response = requests.post(api_endpoint, headers=headers, json=payload)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Return the completion message
    return response.json().get('choices', [{}])[0].get('message', {}).get('content', '').strip()


