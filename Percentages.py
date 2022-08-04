def percentage(temp):
    total = temp.pop(-1)
    for i in range(len(temp)):
        temp[i] = (temp[i] * 100)/total
    return temp