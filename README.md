![](https://img.shields.io/github/issues/cyclothymia/Socials-Email-Checker)
![](https://img.shields.io/github/stars/cyclothymia/Socials-Email-Checker)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# A Social Media Email Link Checker
A simple social media email checking tool that utilises multiprocessing and proxies to check a bulk list of emails.

### Current supported social media
- Instagram
- Twitter

## Requirements & Setup
The required language is Python, and pip libraries currently necessary is just `requests` and `beautifulsoup4`.

## How to use
1. Download `Socials-Email-Checker` using `git clone https://github.com/cyclothymia/Socials-Email-Checker.git` in the terminal.
2. Load in to the directory using `cd Socials-Email-Checker`
3. Run `pip install requests beautifulsoup4` in the terminal.
4. Add HTTPS proxies into "proxylist.txt".
5. Add emails to be checked to "emails.txt"
6. Run `python main.py`
7. A prompt will come up asking for the filename. Enter the filename of the list. If you did step 4, type "emails.txt" and press enter.
8. If an email is linked on the checked social media, the email will be added to a list named after the social media.

## Recommendations
I recommend you purchase HTTPS proxies from a site you trust, that way the proxies used are reliable.
If you don't know anywhere you can purchase HTTPS proxies, you can from https://proxy.webshare.io for reliable and fast proxies.

## Update Logs
### 18 March, 2024
- Updated repository to utilise all tools within `main.py`, making checks faster and more simplified than previously. Snapchat endpoint has been removed.

### 10 March, 2023
- Added a snapchat checker for email checks. Uses an [unsecure api endpoint](https://github.com/JReverse/Snapchat-Email-Checker)

## Future Plans
- Additional Social Medias
- Faster Checks

## Credits and Mentions
[Proxy handler](https://github.com/landoncrabtree/social-checker/blob/master/proxy.py)
