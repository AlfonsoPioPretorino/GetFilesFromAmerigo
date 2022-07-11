from ast import arg
from fileinput import filename
from gettext import find
from time import time
import uiConsoleMess as mx
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
import urllib.request
from tkinter import Tk, filedialog

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def getFileName(href):
    for i in range(len(href)-1, 0, -1):
        if href[i] == "/":
            return href[i+1:]
    return href[1:]

def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)


def startDownload(url, path, FILE_TO_DOWNLOAD):
    import generalDatas
    import uiConsoleMess
    index = 1
    reqs = requests.get(url, stream=True)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get("href")
        if "javascript" not in href and "iTunes" not in href and "#" not in href and FILE_TO_DOWNLOAD in href and href not in generalDatas.getFolders():
            filename = getFileName(link.get("href"))
            print(index, ")", filename)
            urlDownload = generalDatas.getHomeUrl()+href[1:]
            filePath = path+"/"+filename
            download_url(urlDownload, filePath)             
            index += 1
            if FILE_TO_DOWNLOAD != "":
                break
    uiConsoleMess.workFinished()
    input()


def choosePath():
    root = Tk() 
    root.withdraw() 
    root.attributes('-topmost', True) 
    return filedialog.askdirectory() 

def lookUpForContent(soup):
    import generalDatas
    folders = []
    content = []
    for link in soup.find_all('a'):
        hrefSplit = []
        hrefSplit = link.get("href").split(".")
        if len(hrefSplit) ==  1:
            if hrefSplit[0] != "#" and hrefSplit[0] != " " and "javascript" not in hrefSplit[0] and "iTunes" not in hrefSplit[0] :
                folders.append(hrefSplit[0])
            else:
                continue
        elif "javascript" not in link.get("href") and "#" not in link.get("href"):
            content.append(link.get("href"))
    mx.contentPrinter(folders, "ƒ ")
    mx.contentPrinter(content, "■ ")
    generalDatas.setFolders(folders)
    generalDatas.setContents(content)


def navigateTo(destlink):
    import generalDatas
    import sys
    print("════════════════════════════════════════════════════════")
    generalDatas.setCurrentUrl(destlink)
    homeurl = generalDatas.getHomeUrl() 
    try:
        reqs = requests.get(destlink, stream=True)
        navsoup = BeautifulSoup(reqs.text, 'html.parser')
        if destlink == homeurl:
            print("»Posizione attuale »»» Home")
        else:
            print("»Posizione attuale »»» 🗀 ", destlink[len(homeurl):])
        print("════════════════════════════════════════════════════════")
        lookUpForContent(navsoup)
    except:
        mx.generalErr()
        input()
        sys.exit()

def checkCommand(command):
    global commands
    commandsplitted = command.split(" ")
    if commandsplitted[0] not in commands:
        mx.commandInvalid()
    else:
        if len(commandsplitted) > 1:
            executeCommand(commandsplitted[0], command[len(commandsplitted[0])+1:])
        elif len(commandsplitted) == 1:
            executeCommand(command, " ")

def executeCommand(cmd, argument):
    import generalDatas
    import uiConsoleMess
    import sys
    import time
    if cmd == "/nav":
        if argument == " ":
            navigateTo(generalDatas.getHomeUrl())
        else:
            navigateTo(generalDatas.getCurrentUrl()+argument)
    elif cmd == "/back":
        cu = generalDatas.getCurrentUrl()
        for i in range(len(cu)-2, 0, -1):
            if cu[i] == "/":
                newurl = cu[0:i+1]
                break
        navigateTo(newurl)
    elif cmd == "/download":
        if generalDatas.getDownloadPath() == " ":
            generalDatas.setDownloadPath(choosePath())
        if argument == " ":
            startDownload(generalDatas.getCurrentUrl(), generalDatas.getDownloadPath(), "")
        else:
            startDownload(generalDatas.getCurrentUrl(), generalDatas.getDownloadPath(), argument)
        navigateTo(generalDatas.getCurrentUrl())
    elif cmd == "/quit":
        uiConsoleMess.goodbye()
        time.sleep(1)
        sys.exit()
    elif cmd == "/help":
        uiConsoleMess.help()
        input()
        navigateTo(generalDatas.getHomeUrl())


commands = ["/nav", "/back", "/download", "/quit", "/help"]