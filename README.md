# first install python 2.7
# install requests and install beautifulsoup4
# use pip install to download
# I got my information from http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup/

from bs4 import BeautifulSoup

import requests

url = raw_input(//*[@id="stream-item-tweet-932220338808770560"]/div[1]/div[2]/div[3]/div)

r = requests.get("http://"+url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
	print(link.get('href'))
