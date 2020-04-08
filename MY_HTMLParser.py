from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin
from folder import checkFile
import validators

class MyHTMLParser(HTMLParser):

    def __init__(self, url):
        HTMLParser.__init__(self)
        self.links = []
        self.adjLinks = []
        self.adjDict = {}
        self.url = url

    def handle_starttag(self, tag, attrs):
        value = ''
        if tag == "a":
           for name, value in attrs:           
                if name == "href":
                    scheme = urlparse(self.url).scheme
                    host = urlparse(self.url).netloc
                    base = scheme + '://' + host + '/'
                    url = urljoin(base, value)
                    if validators.url(url):
                        self.adjLinks.append(url)
                        if not checkFile(url):
                            if url.split('?')[0].split('#')[0] not in self.links:
                                self.links.append(url.split('?')[0].split('#')[0])

    def removeFromList(self, links):
        self.links.remove(links)






