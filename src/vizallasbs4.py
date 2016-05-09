from lxml import html
from bs4 import BeautifulSoup
import requests
import warnings

proxies = {
  'http': 'http://PITC-Zscaler-EMEA-London3PR.proxy.corporate.gtm.ge.com:80',
  'https': 'https://PITC-Zscaler-EMEA-London3PR.proxy.corporate.gtm.ge.com:80',
}

with warnings.catch_warnings():
            warnings.simplefilter("ignore")

#soup = BeautifulSoup(urlopen('http://www.hydroinfo.hu/tables/dunelot.html'))

#print(soup.prettify())

url = 'http://www.hydroinfo.hu/tables/dunelot.html'             
page =requests.get(url, proxies=proxies)
soup = BeautifulSoup(page.text)
#soup.get_text()
#print(soup)
print(soup.prettify())