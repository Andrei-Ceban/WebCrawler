from robot_file import get_RobotTxt, disallowedPaths, robot_meta
from check import check
from MY_HTMLParser import MyHTMLParser

url = 'https://ok.ru/'

parser = MyHTMLParser(url)

check(url, parser, 0)







