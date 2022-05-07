import urllib.request
from urllib.request import urlopen
import requests
import sys
import io
from bs4 import BeautifulSoup
from sys import stdout

def _restart_line():
    stdout.write('\r')
    stdout.flush()

def startDownload(url):
    index = 1
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    urls = []

    print('--------------------------------------------------------')
    for link in soup.find_all('a'):
        if "javascript" not in link.get('href') and "iTunes" not in link.get('href') and "#" not in link.get('href'):
            print(index, ")", link.get('href'))
            currentLink = link.get('href')
            if " " in link.get('href'):
                continue0
            urlDownload = url+currentLink
            urllib.request.urlretrieve(urlDownload, 'C:/Users/Alfonso/Desktop/test'+currentLink)
            index += 1

url = input("Inserire URL Target. Inserire 0 per usare quello di default.\n")
choice = int(url)
print(choice == 0)
if choice == 0:
    url = 'http://192.168.1.15:8080'
else:
    url = 'http://'+ url

start = int(input("Inserire 1 per avviare.\nInserire 0 per uscire.\n"))


if start == 1:
    startDownload(url)
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
    print("Download terminato con successo.")
else:
    print("Download annullato con successo.")

input("Premi un tasto per chiudere...")
