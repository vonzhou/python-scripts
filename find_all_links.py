import requests
import re

# get url
url = 'http://www.baidu.com'

# connect to the url
website = requests.get(url)

# read html
html = website.text

# use re.findall to grab all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

# or use xpath() to parse <a> tags ...

# output links
for link in links:
    print(link[0])
