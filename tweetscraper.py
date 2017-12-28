from bs4 import BeautifulSoup
import requests
import sys  # for user input

while True:

  url = raw_input(//*[@id="stream-item-tweet-932220338808770560"]/div[1]/div[2]/div[3]/div)

  r = requests.get("http://"+url)

  data = r.text

  soup = BeautifulSoup(data)

  for link in soup.find_all('a'): print(link.get('href'))
  
  print "press CTRL+C to exit program"
  
  interval = 5  # default interval 5 seconds
  
  if len(sys.argv) == 2:   # if user typed an input
    interval = sys.argv[2] # set interval to input
  
  time.sleep(interval)
