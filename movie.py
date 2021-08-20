import os
import sys 
import time as t 
import imdb
import colorama 
import datetime as datetime
from datetime import datetime
from imdb import IMDb
from colorama import Fore 
from colorama import init
import platform
from sys import platform

sys.platform


def bannerwin():
        print(Fore.RED+"----------------------------------------------------")
        print(Fore.RED+"       __                  __                       ")
        print(Fore.RED+".----.|__|.-----.______.--|  |.--.--.--------.-----.")
        print(Fore.RED+"|  __||  ||     |______|  _  ||  |  |        |  _  |")
        print(Fore.RED+"|____||__||__|__|      |_____||_____|__|__|__|   __|")
        print(Fore.RED+"                                             |__|   ")
        print(Fore.BLUE+"---------------------------------------------------")

def cs(X):
	t.sleep(X)
	os.system('cls')

# CHECK THE OS AND THE CURRENT SYSTEM
# IF SYSTEM IS RECONGIZED AS WINDOWS USE COMMAND 'CLS'
# IF SYSTEM IS LINUX CHANGE THE SYS CONFIG OR DEF CONFIG TO USE CLS INSTEAD OF CLEAR FOR / SYSTEMS 
def oscheck():
        if sys.platform == 'linux':
                print(" hello 1 ")
                if sys.platform == 'win-32':
                        def cs(X):
                                t.sleep(X)
                                os.system('cls')
                                if sys.platform == 'win-64':
                                        def cs(X):                                                
                                                t.sleep(X)
                                                os.system('cls')
cs(2)

oscheck()
init() # WINDOW COLOR COMPATIBILITY 

ia = imdb.IMDb()


def bannerwin1():
        print(Fore.RED+"----------------------------------------------------")
        print(Fore.RED+"       __                  __                       ")
        print(Fore.RED+".----.|__|.-----.______.--|  |.--.--.--------.-----.")
        print(Fore.RED+"|  __||  ||     |______|  _  ||  |  |        |  _  |")
        print(Fore.RED+"|____||__||__|__|      |_____||_____|__|__|__|   __|")
        print(Fore.RED+"                                             |__|   ")
        print(Fore.BLUE+"---------------------------------------------------")
	

search = ia.get_top250_movies()
sys.platform

if sys.platform == 'linux':
        bannerwin1()
        if sys.platform == 'darwin':
                bannerwin()
                if sys.platform == 'win32':
                        bannerwin1()
                        if sys.platform == 'win64':
                                bannerwin1()
bannerwin()
for i in range(250):
	print(Fore.RED+"--------------------------------------------------------------|")
	t.sleep(0.3)
	print(Fore.BLUE+'[DATA]  ==>  | ' + str(datetime.now()))
	print(Fore.YELLOW+'[MOVIE] ==> |', search[i],)
