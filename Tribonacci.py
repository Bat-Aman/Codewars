def tribonacci(signature, n):
    if(n == 0):
        return []
    if(n == 1):
        return [signature[0]]
    temp_list = signature[:]
    new_number = 0
    for i in range(0, n - len(signature)):
        new_number  = sum(temp_list)
        signature.append(new_number)
        temp_list.append(new_number)
        temp_list.remove(temp_list[0])
        new_number = 0
        
    return signatur
