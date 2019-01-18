
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
x=0
# Retrieve all of the anchor tags
while x!=7:
    tags = soup('a')
    actual_tag=tags[17]
    #print(actual_tag)
    print(actual_tag.contents[0])
    url=actual_tag.get('href',None)
    html=urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,"html.parser")
    x+=1
"""
for tag in actual_tag:
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    print(tag.contents[0])
    #print('Attrs:', tag.attrs)
"""