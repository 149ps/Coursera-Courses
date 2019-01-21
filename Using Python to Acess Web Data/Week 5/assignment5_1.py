import xml.etree.cElementTree as ET
from urllib.request import urlopen

import ssl
from bs4 import BeautifulSoup


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tree=ET.fromstring(soup.decode())
lst = tree.findall('comments/comment')
sum=0
for item in lst:
    sum+=int(item.find('count').text)
    print(sum)
print(sum)
