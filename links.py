import requests
from MY_HTMLParser import MyHTMLParser

def getLinks(parser):
    res = requests.get(parser.url)
    text = res.text
    parser.feed(text)

    return {'parser': parser, 'links': parser.links}
