import json
from urllib.request import urlopen
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url=input("Enter URL:")
html = urlopen(url, context=ctx).read()
#print(html.decode())
info=json.loads(html.decode())
print(info)
new_info=info["comments"]
sum=0
for item in new_info:
    sum+=item["count"]
print(sum)
    