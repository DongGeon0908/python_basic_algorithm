def find(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)

def sort(a):
    result =[]
    while a:
        value = a.pop(0)
        insert_value = find(result, value)
        result.insert(insert_value, value)
    return result


d = [2, 4, 5, 1, 3]
print(sort(d))
