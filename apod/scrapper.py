# from the archive follow each link.
# find the image in the link and download the image.
import urllib.request

base_url = "http://apod.nasa.gov/apod/archivepix.html"
content = urllib.request.urlopen(base_url).read()
print(content)