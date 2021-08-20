import os 
import time as t 
import imdb
import colorama 
import datetime as datetime
from datetime import datetime
from imdb import IMDb
from colorama import Fore 
from colorama import init

def cs(X):
	t.sleep(X)
	os.system(' clear ')

cs(2)

init()

ia = imdb.IMDb()


def banner():
	print(Fore.BLUE+"")
	os.system('figlet cin-dump ')
	print(Fore.RED+"            V1.0 ")
	print(Fore.RED+" Dumpster diving for movies :D")
	

search = ia.get_top250_movies()

banner()
for i in range(250):
	                #[DATA] ==> | The Lord of the Rings: The Fellowship of the Ring
	print(Fore.RED+"--------------------------------------------------------------|")
	t.sleep(0.3)
	print(Fore.BLUE+'[DATA]  ==>  | ' + str(datetime.now()))
	print(Fore.YELLOW+'[MOVIE] ==> |', search[i],)
