from folder import createMapFile
from folder import getDictFromAdjList
links = getDictFromAdjList()

def map(pageUrl):
    for link in links[pageUrl]:
        createMapFile(link, pageUrl)
        return 0

# def map(idPage, pageList):
#     output = []
#
#     for page in pageList:
#         output.append((page, idPage))
#
#     return output
#
#     # a si d arata spre b