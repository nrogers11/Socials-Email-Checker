import asyncio

from src.tools import Tools
from src.proxy import workingProxy
from multiprocessing import Pool, freeze_support
from requests.structures import CaseInsensitiveDict

os.system('cls' if os.name == 'nt' else 'clear')
print("[ GitHub ++ https://github.com/cyclothymia/Socials-Email-Checker ]")

def run_async(email):
    async def main(email):
        tools = Tools()
        await tools.instagram(email)
        await tools.twitter(email)

    asyncio.run(main(email))

def process_email(line):
    email = line.strip()
    run_async(email)

if __name__ == '__main__':
    freeze_support()
    filename = input("Enter the email filename: ")
    
    with open(filename) as f:
        emails = f.readlines()

    with Pool(processes=100) as pool:
        pool.map(process_email, emails)
