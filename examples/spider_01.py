"""
requests 库的使用
"""
import requests

def request_demo(url):
    """
    
    """
    response = requests.get(url)
    ret = response.text

    return ret

if __name__ == "__main__":
    url = 'https://image.so.com/'
    response = request_demo(url)

    print(response)