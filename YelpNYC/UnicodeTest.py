from bs4 import BeautifulSoup
import requests

url = "https://www.yelp.com/search?find_loc=New+York,+NY,+US&start=0&cflt=restaurants"

req = requests.get(url)
soup = BeautifulSoup(req.content, "lxml")

bn = [d.span.contents[0].encode('utf-8') for d in soup.find_all("a", {"class": "biz-name"})]
rating = [d['title'].strip('star rating') for d in soup.find_all("div", {"class":"i-stars"})]
price = [d.contents[0] for d in soup.find_all("span",{"class":"price-range"})]
area = [d.contents[0].strip() for d in soup.find_all("span", {"class":"neighborhood-str-list"})]
addr = [d.contents[0].strip() for d in soup.find_all("address")]
#bn = [ d.decode('utf-8') for d in bn]
res = [d for d in zip(bn, rating, price, area, addr)]

print bn
