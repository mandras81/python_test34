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

#url = 'http://www.hydroinfo.hu/tables/dunelot.html'
url = 'http://econpy.pythonanywhere.com/ex/001.html'
page =requests.get(url, proxies=proxies)

#tree = page.text

tree = html.fromstring(page.content)
#This will create a list of buyers:
#kiadva = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')

#print ('Buyers: ', buyers)
#print ('Prices: ', prices)

#kiadva = tree.xpath('//table/tbody/tr[1]/td/div/font/strong/text()')
kiadva = tree.xpath('//table/tbody/tr/td[1]/div/font/text()')
#//table/tbody/tr/td[1]/div/font
#//table/tbody/tr/td/div/font/b

print(kiadva)
