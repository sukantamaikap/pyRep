# from the archive follow each link.
# find the image in the link and download the image.
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

base_url = "http://apod.nasa.gov/apod/archivepix.html"
download_dir = "apod_images"

content = urllib.request.urlopen(base_url).read()
a_tags = BeautifulSoup(content, "lxml").findAll("a")
print("get all the images ...")
for a in a_tags :
    image_page_url = urljoin(base_url, a["href"])
    #get the image from the url
    content = urllib.request.urlopen(image_page_url).read()
    for image in BeautifulSoup(content, "lxml").findAll("img"):
        image_url = urljoin(base_url, image["src"])
        print("image url found : ", image_url)
        image_name = image_url.split("/")[-1]
        print("image name : " + image_name)
        if "calendar" in str(image_url):
            print("Invalid image url found, skipping this : ", image_url)
            continue
        urllib.request.urlretrieve(image_url, os.path.join(download_dir, image_name))
