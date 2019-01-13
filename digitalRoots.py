def digital_root(n):
    l1 = [int(i) for i in str(n)]
    result = sum(l1)    
    if (result >= 10):
        return digital_root(result)
    else:
        return result
