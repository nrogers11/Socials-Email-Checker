import os, time, asyncio, aiohttp, requests
from src.proxy import workingProxy
from bs4 import BeautifulSoup

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Tools:
    async def instagram(self, mail):
        email = mail
        proxy = workingProxy()
        proxies = {
            "http": "http://" + proxy
        }
        r = requests.Session()
        url = "https://www.instagram.com/accounts/account_recovery_send_ajax"
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        r.headers = {'User-Agent': useragent}
        r.headers.update({'X-CSRFToken': 'missing'})
        data = {"email_or_username": email}
        req = r.post(url, data=data, proxies=proxies)
        print(req.text)
        print('')
        if req.text.find("We sent an email to")>=0:
            file = open("instagram-linked.txt", "a")
            file.write(email + "\n")
            file.close()
            print(bcolors.OKGREEN + f"{email} = is linked to an account" + "\n" + bcolors.ENDC)
        elif req.text.find("password")>=0:
            file = open("instagram-linked.txt", "a")
            file.write(email + "\n")
            file.close()
            print(bcolors.OKGREEN + f"{email} = is linked to an account" + "\n" + bcolors.ENDC)
        elif req.text.find("sent")>=0:
            file = open("instagram-linked.txt", "a")
            file.write(email + "\n")
            file.close()
            print(bcolors.OKGREEN + f"{email} = is linked to an instagram account" + "\n" + bcolors.ENDC)
        else:
            print(bcolors.WARNING + f"{email} = is not linked to an instagram account" + "\n" + bcolors.ENDC)
    
    async def twitter(self, mail):
        email = mail
        proxy = workingProxy()
        proxies = {
            "http": "http://" + proxy
        }
        r = requests.Session()
        url = "https://api.twitter.com/i/users/email_available.json?email=" + email
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
        Host = "api.twitter.com"
        Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        r.headers = {'User-Agent': useragent}
        r.headers = {'Host': Host}
        r.headers = {'Accept': Accept}
        req = r.get(url, proxies=proxies).json()
        text = str(req)

        print('')
        if text.find("'valid': False") == True:
            file = open("twitter-linked.txt", "a")
            file.write(email + "\n")
            file.close()
            print(bcolors.OKGREEN + f"{email} = is linked to a twitter account" + "\n" + bcolors.ENDC)
        else:
            print(bcolors.WARNING + f"{email} = is not linked to a twitter account" + "\n" + bcolors.ENDC)
