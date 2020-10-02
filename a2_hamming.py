import hashlib, sys

def hammingdistance(hex1, hex2):
    if not isinstance(hex1, basestring) or not isinstance(hex2, basestring):
        sys.exit()

    hamdist = 0
    #cloning
    h1 = hex1
    h2 = hex2
    #turns our hex strings into binary strings
    h1 = bin(int(h1, 16)).zfill(8)
    h2 = bin(int(h2, 16)).zfill(8)

    k = len(h1)
    #loop the indices of the string
    for i in range(k):
        if h1[i] != h2[i]:
            hamdist += 1

    return hamdist




#m = hashlib.sha256()
#m.update(b"Nobody inspects")
#print m.hexdigest()
