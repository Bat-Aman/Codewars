def create_phone_number(n):
    state_code = ''.join(str(x) for x in n[:3])
    next_three = ''.join(str(x) for x in n[3:6])
    last_four = ''.join(str(x) for x in n[6:10])
    
    output_str = '(' + state_code + ')' + ' ' + next_three + '-' + last_four
    return output_str
