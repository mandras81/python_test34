from lxml import html
import requests
import warnings


proxies = {
  'http': 'http://PITC-Zscaler-EMEA-London3PR.proxy.corporate.gtm.ge.com:80',
  'https': 'https://PITC-Zscaler-EMEA-London3PR.proxy.corporate.gtm.ge.com:80',
}

with warnings.catch_warnings():
            warnings.simplefilter("ignore")


# url = 'https://www.vizugy.hu/index.php?module=content&programelemid=138'
url = 'http://www.hydroinfo.hu/tables/dunelot.html'             
page =requests.get(url, proxies=proxies)
tree = html.fromstring(page.content)
#tree = page.text
#text = tree.XPath("//text()")
#text = find_text(Kiadva[0])
#This will create a list of buyers:
#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
#prices = tree.xpath('//span[@class="item-price"]/text()')

#print ('Buyers: ', buyers)
#print ('Prices: ', prices)

#kiadva = tree.xpath('//tr[5]/td/div/font/b/text()')
datum = tree.xpath('//tr[3]/td[position()>1]/div/font/b/text()')
kiadva = tree.xpath('//tr[5]/td/table/tr/td/div[@align="right"]/font/b/text()')

#kiadva.remove('128')
print(datum)
print(kiadva)
#count = 0
#while (count < len(kiadva)):
#   print 'The count is:', count
#   count = count + 1

#/html/body/table/tbody/tr[5]/td[3]/table/tbody/tr/td[1]/div/font/b