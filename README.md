# Scraping And Data Analysis

### start here
read up on xpath, its has a bit has an approach to child element access similar to that of CSS, for a lack of better works. Its relatively short and should be easy to understand given some experience and/or knowledge of SQL
* https://www.w3schools.com/xml/xpath_intro.asp

next you'll want to watch this video for some brief introduction.
* https://www.youtube.com/watch?v=1EFnX1UkXVU
* https://www.youtube.com/watch?v=3xQTJi2tqgk

after that, you'll need to download and install scrapy for python; [get it here](https://docs.scrapy.org/en/latest/). The next thing you'll need is Beautiful Soup, also for python, it's used to parse HTML tags and data; [get it here](https://www.crummy.com/software/BeautifulSoup/).

when you have those things, we can begin to look into the documentation of scrapy, we'll devise a plan on how and what to do with the implement our scraper/spider.

==

next you'll want to install the necessary components to access your MySQL server

* `pip install MySQL-python`
* `pip install mysql-connector-python`
* `pip install pymysql`
