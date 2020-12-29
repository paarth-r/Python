
missisipi = ["m",'i','s','s','i','s','i','p','i']


		


def counti(word):
    count = 0
    for i in word:
        if i is 'i':
            count+=1

    return count

def lastletter(mis):
    return mis[-1]

c = lastletter(missisipi)
print(c)


