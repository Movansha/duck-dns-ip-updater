import requests, webbrowser

def get_IP():
    try:
        return requests.get('https://api.ipify.org').text
    except:
        return "Unknown"

def update_IP(domain, token):
    try:
        response = requests.get(f"https://www.duckdns.org/update/{domain}/{token}")
        if response.text == "OK":
            return "Success"
        return "Failed"
    
    except:
        return "Failed"

def open_Site():
    webbrowser.open("https://www.duckdns.org")
