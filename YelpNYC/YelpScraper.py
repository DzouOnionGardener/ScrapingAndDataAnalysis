import scrapy
import requests
from bs4 import BeautifulSoup

url = "https://www.yelp.com/search?cflt=restaurants&find_loc=New+York%2C+NY%2C+US"
req = requests.get(url)
soup = BeautifulSoup(req.content)

#<a class="biz-name"> : child span
#<div class="i-stars" title="# of stars">
#<span class="price-range">
#<div class="secondary-attribute">
#<span class="neighborhood-str-list>
#<address>

bizName = soup.find_all("a", {"class":"biz-name"})
bizRating = soup.find_all("div", {"class":"i-stars"})
priceRange = soup.find_all("span",{"class":"price-range"})
SecondaryAttr = soup.find_all("div", {"class:secondary-attribute"})
bizAddr = soup.find_all("address")

for names in bizName:
    print names.text

for ratings in bizRating:
    print ratings["title"]

for price in priceRange:
    print price.text

for addr in bizAddr:
    print addr.text

