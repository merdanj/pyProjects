#Author: Merdan Jumanov
#Date: 23/05/18
#Purpose: Learning how to download images with BeautifulSoup, urllib and etc.
from bs4 import BeautifulSoup
from urllib.request import urlopen 
from urllib.request import Request
import re
import os

# Download parameters
image_type = "Project"
movie = "Avatar"
url = "https://www.google.com/search?q="+movie+"&source=lnms&tbm=isch"

header = {'User-Agent': 'Mozilla/5.0'}
soup = BeautifulSoup(urlopen(Request(url, headers=header)))

image = [a['src'] for a in soup.find_all("img", {"src":re.compile("gstatic.com")})][:5]
for img in image:
    # print ("Image Source:", img)
    raw_img = urlopen(img).read()
    cntr = len([i for i in os.listdir(".") if image_type in i]) + 1
    f = open(image_type+"_"+str(cntr)+".jpg", 'wb')
    f.write(raw_img)
    f.close
