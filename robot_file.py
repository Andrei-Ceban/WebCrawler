import requests
from bs4 import BeautifulSoup

def get_RobotTxt(url):
    res = requests.get(url+"/robots.txt")
    return res.text

def disallowedPaths(robFile):
    soup = BeautifulSoup(robFile, 'html.parser')
    res = []
    collect = False
    for index, item in enumerate(str(soup).split('\n')):
        if collect and str(item).startswith('Dis'):
            path = item.split(':')[1].strip()
            if path != '':
                if path[-1] == '?':
                    path = path[0:-1]
            res.append(path)
        if str(item).lower().startswith('user'):
            if item.strip().upper() == 'USER-AGENT: *':
                collect = True
            else:
                collect = False

    return res

def robot_meta(url):
    res = requests.get(url)
    text = res.text
    soup = BeautifulSoup(text, 'html.parser')

    for i in soup.findAll('meta'):
        if i.get('name') == 'robots':
            return str(i.get('content'))
    return ''
