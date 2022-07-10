def getHomeUrl():
    global homeurl
    return homeurl

def setHomeUrl(newurl):
    global homeurl
    homeurl = "http://"+newurl+":8080/"

def setCurrentUrl(url):
    global currenturl
    currenturl = url

def getCurrentUrl():
    global currenturl
    return currenturl

def setDownloadPath(newpath):
    global path
    path = newpath

def getDownloadPath():
    global path
    return path

def getContents():
    global contents
    return contents

def setContents(currentcontents):
    global contents
    contents = currentcontents

def getFolders():
    global folders
    return folders
    
def setFolders(currentfolders):
    global folders
    folders = currentfolders

def addToIgnore(string):
    global ignore
    ignore.append(string)

def getIgnore():
    global ignore
    return ignore

homeurl = "http://192.168.1.55:8080/"
currenturl = ""
path = " "
folders = []
contents = []
ignore = ["iTunes", "#", "javascript"]