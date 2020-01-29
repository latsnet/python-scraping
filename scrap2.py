from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = "https://www.alura.com.br"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

try:
    req = Request(url, headers = headers)
    response = urlopen(req)
    html = response.read()
    print(html)

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)