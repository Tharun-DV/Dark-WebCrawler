from stem import Signal
from stem.control import Controller
from requests import get
from fake_useragent import UserAgent
from getpass import getpass
def new_tor_id(passw):
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password=passw)
        controller.signal(Signal.NEWNYM)

def new_identity(url):
    tor_proxy = {
        "http": "socks5h://localhost:9050",
        "https": "socks5h://localhost:9050"
    }
    headers = {
        "User-Agent": UserAgent().random
    }
    resp = get(url, headers=headers, proxies=tor_proxy)
    return resp

def connect(url,passw):
    new_identity(url)
    new_tor_id(passw)