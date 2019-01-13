def count_smileys(arr):
    counter = 0
    valid_faces = [':)', ':-)', ':~)', ':D', ':-D', ':~D', ';)', ';-)', ';~)', ';D', ';-D', ';~D']
    for i in arr:
        if i in valid_faces:
            counter += 1
    return counter
