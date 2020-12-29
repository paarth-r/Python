def dig_count(n):
    counter =  0
    while n != 0:
        n //= 10
        counter += 1
    return counter
        


def even_dig_nums(nums):
    d = {'even':[], 'odd':[]}
    for n in nums:
        num = dig_count(n)
        if num % 2 == 0:
            d.get('even').append(n)
        else:
            d.get('odd').append(n)
            
    return (d)
        
            
