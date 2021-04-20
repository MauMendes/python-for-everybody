# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def GetNextUrl( url, pos):
    if pos<1:
        return ""

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    
    url_list = list()
    for tag in tags:
        url_list.append( tag.get('href', None))
    
    #print("Getting url:", url, "position:", pos)
    if len(url_list)>=pos:
        return url_list[pos-1]
    else :
        return ""


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#first_url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
first_url = "http://py4e-data.dr-chuck.net/known_by_Rayhan.html"
print(first_url)
x = GetNextUrl(first_url, 18)
print(x)

for items in range(6):
    y = GetNextUrl(x, 18)
    print(y)
    x = y