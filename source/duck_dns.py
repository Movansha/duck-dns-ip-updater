import requests, webbrowser


def get_IPv4():
    try:
        return requests.get('https://api.ipify.org').text
    except:
        return "Unknown"
    
def get_IPv6():
    try:
        adress = requests.get('https://api64.ipify.org').text

        if (adress != get_IPv4()):
            return adress
        return "Unknown"
    
    except:
        return "Unknown"
    


def update_IP(domains, token):
    try:
        IPv4_adress = get_IPv4()
        IPv6_adress = get_IPv6()

        ip_adresses = "&ip=" + IPv4_adress

        if IPv6_adress != "Unknown":
            ip_adresses += "&ipv6=" + IPv6_adress

        response = requests.get(f"https://www.duckdns.org/update?domains={domains}&token={token}{ip_adresses}")

        if response.text == "OK":
            return "Success"
        return "Failed"
    
    except:
        return "Failed"

def open_Site():
    webbrowser.open("https://www.duckdns.org")
