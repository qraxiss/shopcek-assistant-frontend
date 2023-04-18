import requests

from config import API_URI

def api(path: str, body: dict, method: str) -> requests.Response:
    return requests.request(method=method,
                     url=f'{API_URI}/{path}',
                     json=body)
