import scrapy
import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.yelp.com/search?cflt=restaurants&find_loc=New+York%2C+NY%2C+US"
"""
we're going to use parse data from the first 20 pages
store that data into CSV files
then we'll also store that data into a mySQL database
execute some basic queries on it
===
we'll then learn how to use pandas and matplotlib to graph that data
"""

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
SecondaryAttr = soup.find_all("div", {"class":"secondary-attribute"})
bizNeighborhood = soup.find_all("span", {"class":"neighborhood-str-list"})
bizAddr = soup.find_all("address")

for names in bizName:
    print names.text

for ratings in bizRating:
    print ratings["title"]

for price in priceRange:
    print price.text

for addr in bizAddr:
    print addr.text.lstrip()

for n in bizNeighborhood:
    print n.text.lstrip()