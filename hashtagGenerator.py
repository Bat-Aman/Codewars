def generate_hashtag(s):
    output_string = '#'
    if s == '' or len(s) > 140:
        return False
    else:
        s = s.title()
        s = list(s)
        for i in s:
            if i != ' ':
                output_string += i
        return output_string
