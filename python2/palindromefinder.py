def is_palindrome(word):
    half1 = word[0:len(word)//2]
    half2 = word[len(word)//2: len(word)]
    h1_i= 0
    if len(word) % 2 != 0:
        half2 = half2[1:len(half2)]
    for h2_i in range(len(half2)-1,-1,-1):            
        print("h2: ", h2_i, half2[h2_i])
        print("h1: ", h1_i, half1[h1_i])
        if half2[h2_i] != half1[h1_i]:
            return False
        h1_i += 1
    return True

print(is_palindrome("0ba5ab0"))


"""

h1 = ab0
     012
h2 = 0ba
     012

h1 == reverse h2: palindrome
h1 != reverse h2: not palindrome



"""



            
            
        


    
    
    
    
