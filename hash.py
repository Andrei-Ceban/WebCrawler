import hashlib

def addToJSONfile(link, digest):
    with open('link_digest.txt', "a", encoding='utf-8') as file:
        file.write(link+': '+digest+'\n')
    file.close()

def getId(link):    
    m = hashlib.sha1()

    m.update(link.encode('utf-8'))
    addToJSONfile(link, m.hexdigest())

    return m.hexdigest()

