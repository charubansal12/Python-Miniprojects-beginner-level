#Code to download image from a url to the computer


import random
import urllib.request

def download_image_from_web(url):
    name = random.randrange(1,1000)
    full_name= str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)


download_image_from_web("https://scontent.cdninstagram.com/hphotos-xpa1/t51.2885-15/e35/12317306_551965408291326_1700749533_n.jpg")
