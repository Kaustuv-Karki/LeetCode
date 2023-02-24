def digitize(n):
    arr = []
    for i in str(n):
        arr.append(int(i));
    return arr[::-1]