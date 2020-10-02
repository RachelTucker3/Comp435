import sys, hashlib, random, string
def find_preimage(target, n):
    #counter = 0
    # grab input's first n bits
    while True:
        # generate random string
        match = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        match = match.encode('ascii')

        m = hashlib.sha256(match)
        mDigest = m.digest()
        #counter += 1
        #checks if the hashed strings are the same to the nth point
        if mDigest[:n] == target[:n]:
            #print counter
            return match
        else:
            continue
if __name__ == '__main__':
    msg = "The quick brown fox jumps over the lazy dog."
    hashed = hashlib.sha256(msg.encode('ascii'))
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)
    print find_preimage(hashed.digest(), 2)