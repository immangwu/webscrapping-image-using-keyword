from selenium import webdriver
import os
import urllib
import urllib.request
searchterm = 'single Orange'#input your search item here
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
browser = webdriver.Chrome()#insert path to chromedriver inside parentheses
browser.get(url)
img_count = 0
extensions = { "jpg", "jpeg", "png", "gif" }
if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(1000):
    browser.execute_script("window.scrollBy(0,10000)")
    
html = browser.page_source.split('["')
imges = []
for i in html:
    if i.startswith('http') and i.split('"')[0].split('.')[-1] in extensions:
        imges.append(i.split('"')[0])
count=170;
for j in imges:
    try:
        print(j)
        urllib.request.urlretrieve(j, str(count)+".jpg")
        count=count+1;
        print(count)
    except:
        pass
    
#print(imges)
