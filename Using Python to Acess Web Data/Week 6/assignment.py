"""import urllib.request, urllib.parse, urllib.error
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://conferences.oreilly.com/oscon/oscon-or/public/schedule/speakers"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
"""
from PIL import Image
import requests
import IPython
from io import BytesIO

url="https://www.iottechexpo.com/europe/wp-content/uploads/2019/05/Sak-Nayagam.jpg"
IPython.display.Image(url, width = 250)
