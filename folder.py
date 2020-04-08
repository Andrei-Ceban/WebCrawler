import os
from urllib.parse import urlparse
from hash import getId

def createFile(url):
    if len(url) > 232:
        return 0
    pwd = os.getcwd()
    scheme = urlparse(url).scheme
    host = urlparse(url).netloc
    base = scheme + '://' + host
    path = urlparse(url).path.replace('/','\\')

    filePath = pwd+'\\'+scheme+'\\'+host+path

    if filePath[-1] == '\\':
        filePath = filePath[0:-1]

    folderPath = '\\'.join(filePath.split("\\")[0:-1])
    filePath = filePath.split("\\")[-1]

    for ind, folder in enumerate(folderPath.split('\\')[1:]):
        if not os.path.isdir('\\'.join(folderPath.split('\\')[0:ind+2])):
            os.makedirs('\\'.join(folderPath.split('\\')[0:ind+2]))

    filePath = os.path.join(folderPath+'\\'+filePath+'File')
    if not os.path.isfile(filePath):
        with open(filePath, 'w') as file: pass
        file.close()
        return 'Created'

def checkFile(url):
    url = url.replace('://','/')
    if url[-1] == '/':
        url = url[0:-1] + 'File'
    else:
        url = url + 'File'
    return os.path.isfile(url)

def createAdjList(parser, url, links):
    with open('adjListTest.txt', 'a', encoding='utf-8') as file:
        file.write(getId(url)+':: [')
        for ind, link in enumerate(links):
            file.write(getId(link))
            if ind != len(links) - 1:
                file.write(',')
        file.write(']\n')
        parser.adjLinks = []
    file.close()

def getDictFromAdjList():
    dictionar = {}
    with open('adjList.txt', 'r', encoding='utf-8') as file:
        fileLines = file.readlines()
        for line in fileLines:
            line = line[0:-1]
            dictionar[line.split('::')[0]] = line.split('::')[1].strip()[1:-1].split(',')
    file.close()
    return dictionar

def createMapFile(link, url):
    if not os.path.isfile('./mapFIlesTest/'+link+'_'+url):
        with open('./mapFIlesTest/'+link+'_'+url, 'w', encoding='utf-8') as file:
          pass
        file.close()
def getLinkFromHash(hash):
    with open('link_digest.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if hash in line:
                return line.split(': ')[0]

def getLinksFromMapFiles():
    path = os.getcwd() + '\mapFIles'
    links = set()
    for i in os.listdir(path):
        links.add(i.split('_')[0])
    return links