import urllib.request
from urllib.request import urlopen
import requests
import sys
import io
from bs4 import BeautifulSoup
from sys import stdout
from tqdm import tqdm
from tkinter import Tk, filedialog



class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def choosePath():
    root = Tk() 
    root.withdraw() 
    root.attributes('-topmost', True) 
    return filedialog.askdirectory() 

def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

def startDownload(url, path):
    index = 1
    reqs = requests.get(url, stream=True)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    urls = []

    print('--------------------------------------------------------')
    for link in soup.find_all('a'):
        if "javascript" not in link.get('href') and "iTunes" not in link.get('href') and "#" not in link.get('href'):
            print(index, ")", link.get('href'))
            currentLink = link.get('href')
            if " " in link.get('href'):
                continue
            urlDownload = url+currentLink
            filePath = path+currentLink
            download_url(urlDownload, filePath)
            
                        
            index += 1


print("╔═════════════════════════════════════════════════════════════════════════════════╗")
print("║░░░░░░░░░░░░░░░░░░░░░░░░░░░GET FILES FORM AMERIGO░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║")
print("║                                By Fonzi-Lab                                     ║")
print("║                     GitHub: https://github.com/Fonzi-Lab                        ║")
print("╚═════════════════════════════════════════════════════════════════════════════════╝")

url = input("Inserire URL Target. Inserire 0 per usare quello di default.\n")

if url == 0:
    url = 'http://192.168.1.15:8080'
else:
    url = 'http://'+ url
print("Scegliere la cartella in cui si desidera salvare i file")
path = choosePath()
start = int(input("Inserire 1 per avviare.\nInserire 0 per uscire.\n"))


if start == 1:
    startDownload(url, path)
    print("╔═════════════════════════════════════════════════════════════════════════════════╗")
    print("║                      Download terminato con successo.                           ║")
    print("║                        Premi un tasto per chiudere...                           ║")
    print("╚═════════════════════════════════════════════════════════════════════════════════╝")
    
else:
    print("╔═════════════════════════════════════════════════════════════════════════════════╗")
    print("║                      Download annullato con successo.                           ║")
    print("║                        Premi un tasto per chiudere...                           ║")
    print("╚═════════════════════════════════════════════════════════════════════════════════╝")
    
input()
