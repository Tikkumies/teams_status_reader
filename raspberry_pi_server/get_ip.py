import subprocess

def get_network_adapters():
    text = subprocess.run("ifconfig", capture_output=True)
    return str(text)

def parse_wlan_from_ifconfig(text):
    after_wlan = text.partition("wlan0: ")
    after_inet = after_wlan[2].partition("inet ")
    result = after_inet[2].partition(" ")
    return result[0]
