import requests
import json

def get_cookie():
    return requests.get("https://opentip.kaspersky.com/ui/checksession").headers["Set-Cookie"]

def query_kaspersky(target_url):
    headers = {
        "Cookie": get_cookie(),
        "Content-Type": "application/octet-stream",
    }
    data = ('{"query":"%s","silent":true}' % target_url).encode("utf-8")
    return requests.post("https://opentip.kaspersky.com/ui/lookup", headers=headers, data=data).json()

def main():
    url = input("Enter a valid URL or IP: ").strip()
    print(json.dumps(query_kaspersky(url), indent=2))

if __name__ == "__main__":
    main()
