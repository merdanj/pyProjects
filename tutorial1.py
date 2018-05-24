#Author: Merdan Jumanov
#Date: 22/05/18
#Purpose: first python tutorial. 
from lxml import html
import requests
import bs4

page = requests.get('https://github.com/pricing/')
tree = html.fromstring(page.content)
print("Page Object:", tree)
plans = tree.xpath('//h2[@class="alt-h3"]/text()')
pricing = tree.xpath('//span[@class="default-currency"]/text()')
print("Plans:", plans, "\nPricing:", pricing)


myfile = open('python.html')
soup = bs4.BeautifulSoup(myfile, 'lxml')
#Making the soup
print ("BeatifulSoup Object:", type(soup))

#Find Elements By tags
print (soup.find_all('a'))
print (soup.find_all('strong'))
#Find Elements By id
print (soup.find('div', {"id":"inventor"}))
print (soup.select('#inventor'))
#Find Elements by css print
print (soup.select('.wow'))

print ("\nFacebook URL: ", soup.find_all('a')[0]['href'])
print ("Inventor: ", soup.find('div', {"id":"inventor"}).text)
print ("Span content:", soup.select('span')[0].getText())