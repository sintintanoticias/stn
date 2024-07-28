import requests
import json

API_KEY = '7005a6609b9a4b0a8c3a0e35124817d4'  # Your provided NewsAPI key
URL = 'https://newsapi.org/v2/top-headlines'

def fetch_news():
    params = {
        'apiKey': API_KEY,
        'language': 'es',
        'country': 'do'  # Dominican Republic
    }
    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        news_data = response.json()
        with open('news.json', 'w', encoding='utf-8') as f:
            json.dump(news_data, f, ensure_ascii=False, indent=4)
        print("News fetched and saved successfully.")
    except requests.RequestException as e:
        print(f"An error occurred with the request: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

if __name__ == "__main__":
    fetch_news()
