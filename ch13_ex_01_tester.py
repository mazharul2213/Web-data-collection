import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl

#handling ssl error certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#sending request for datq
url = input("Enter URL: ")
if len(url) < 1:
    url = "http://dr-chuck.com"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

all_data = ET.fromstring(soup)
for data in all_data:
    print(data)