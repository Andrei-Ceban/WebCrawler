from map import map
from reduce import reduce
from folder import getDictFromAdjList, getLinkFromHash
from folder import getLinksFromMapFiles

links = getDictFromAdjList()

# resAfterMap = []

for link in links:
    map(link)

reverseLinks = getLinksFromMapFiles()

for link in reverseLinks:
    result = reduce(link)
    if len(result) > 0:
        print(getLinkFromHash(link), end=" ")
        # print(result,end=" ")
        print(' rank: '+str(len(result)))


