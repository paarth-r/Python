def ifprime(num):
    if num == 2:
        return True
    ran = range(2, num)
    for n in ran: 
        if num % n == 0:
            return False
    return True

print(ifprime(982451653))
