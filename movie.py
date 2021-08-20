import os 
import time
import imdb
import colorama 
from colorama import Fore 
from colorama import init

init()


ia = imdb.IMDb()


search = ia.get_top250_movies()

for i in range(250):
    time.sleep(0.1)
    print(Fore.RED+".............")
    print(Fore.BLUE+"")
    print(search[i])
