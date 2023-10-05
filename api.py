import requests

def get_url(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        content = response.text
        return status_code, content
    except requests.exceptions.RequestException as e:
        print(f"Error making GET request: {e}")
        return None, None
