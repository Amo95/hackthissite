import urllib.request as req
from sys import exit

while True:
    about_page = req.urlopen("http://localhost/builds-hackme/www/about.php").read()
    if b"KEY" in about_page:
        print(about_page)
        exit(0)