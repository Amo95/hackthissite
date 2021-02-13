import urllib.request as req
from sys import exit

def walled(username):
    walled_garden = req.urlopen(f"http://localhost/builds-hackme/www/walled_garden.php?name={username}").read()
    walled_garden_str = walled_garden.decode("utf-8")

    first_split = walled_garden.split("<pre>")
    print(walled_garden_str)

    

   

if __name__ == '__main__':
    username = input("Enter username: ")
    walled(username)