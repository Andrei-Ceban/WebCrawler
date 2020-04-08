import os

path = os.getcwd() + '\mapFIles'

def reduce(pageId):
    inbound = []
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)) and pageId in i:
            inbound.append(i.split('_')[1])
    return inbound

# def reduce(pageId,mapResult):
#     inbound = []
#
#     for pair in mapResult:
#         if pair[0] == pageId:
#             inbound.append(pair[1])
#
#     return inbound