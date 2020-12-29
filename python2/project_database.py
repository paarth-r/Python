def reverse_string(word):
    returnstr = ''
    for n in range(0,len(word)): 
        returnstr = word[n] + returnstr
    return returnstr
