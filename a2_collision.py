import sys, hashlib, random, string

def find_collision(n):
    #counter = 0
    #tracking helper
    hasher = {}
    #generate random strings
    match = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
    match = match.encode('ascii')
    hashed = hashlib.sha256(match)
    hd = hashed.digest()

    #generated hash and stored
    hasher[hd[:n]] = hashed
    #counter+=1

    #generates hashes till collision
    while True:
        match = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(16)])
        match = match.encode('ascii')
        hashed = hashlib.sha256(match)
        hd = hashed.digest()

        if hd[:n] in hasher:
            #print counter
            return match, hasher[hd[:n]]


        else:
            hasher[hd[:n]] = hashed
            #counter += 1
            continue

if __name__ == '__main__':
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)
    print find_collision(2)


