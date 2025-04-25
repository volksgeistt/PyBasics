import requests

web = " " # add the web the url you want

payloads = ["/index.html", "/script.js"] # add more here

for payload in payloads:
    URL = web + payload
    response = requests.get(URL)
    if response.status_code == 200:
        print(f"[ Accessed @ {URL} ]")
        print(response.text)
    else:
        print(f"[ Denied @ {URL} ]")
