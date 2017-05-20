import scrapy
import requests
from bs4 import BeautifulSoup
import csv
"""
we're going to parse data from the first 100 pages
store that data into CSV files
then we'll also store that data into a mySQL database
execute some basic queries on it
===
we'll then learn how to use pandas and matplotlib to graph that data
"""
#url = "https://www.yelp.com/search?find_loc=New+York,+NY,+US&start=0&cflt=restaurants"
## 'start=' iterates by 10
"""
bizName = soup.find_all("a", {"class":"biz-name"})
bizRating = soup.find_all("div", {"class":"i-stars"})
priceRange = soup.find_all("span",{"class":"price-range"})
SecondaryAttr = soup.find_all("div", {"class":"secondary-attribute"})
bizNeighborhood = soup.find_all("span", {"class":"neighborhood-str-list"})
bizAddr = soup.find_all("address")

for names in bizName:
    print names.text
for r in bizRating:
    print r["title"]
for price in priceRange:
    print price.text
for addr in bizAddr:
    print addr.text.lstrip()
for n in bizNeighborhood:
    print n.text.lstrip()
"""
class Yelp(object):
    def __init__(self):
        self.baseURL = "https://www.yelp.com/search?find_loc=New+York,+NY,+US&start="
        self.pageIndex = 0
        self.endURL = "&cflt=restaurants"
        with open('results.csv', 'w') as csvfile:
            self.writer = csv.writer(csvfile)
            self.writer.writerow(["Restaurant", "Rating", "Price_Range", "Area", "Address"])

    # <a class="biz-name"> : child span
    # <div class="i-stars" title="# of stars">
    # <span class="price-range">
    # <div class="secondary-attribute">
    # <span class="neighborhood-str-list>
    # <address>
    def generateCSV(self):
        while(self.pageIndex < 200):
            url = self.baseURL + str(self.pageIndex) + self.endURL
            req = requests.get(url)
            soup = BeautifulSoup(req.content)
            ##
            bn = [d.span.contents for d in soup.find_all("a", {"class":"biz-name"})]
            rating = [d['title'].strip('star rating') for d in soup.find_all("div", {"class":"i-stars"})]
            price = [d.contents[0] for d in soup.find_all("span",{"class":"price-range"})]
            area = [d.contents[0].strip() for d in soup.find_all("span", {"class":"neighborhood-str-list"})]
            addr = [d.contents[0].strip() for d in soup.find_all("address")]
            res = [d for d in zip(bn, rating, price, area, addr)]
            with open('results.csv', 'a') as d:
                self.writer = csv.writer(d)
                try:
                    for e in res:
                        self.writer.writerow(e)
                except:
                    pass
            self.pageIndex += 10

if __name__ == "__main__":
    y = Yelp()
    y.generateCSV()