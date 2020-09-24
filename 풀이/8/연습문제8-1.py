def find_max(a):
    n = len(a)
    max = 0
    for i in range(1, n):
        if a[i] > a[max]:
            max = i
    return max

def sort(a):
    result = []
    while a:
        max = find_max(a)
        value = a.pop(max)
        result.append(value)
    return result


d = [2, 4, 5, 1, 3]
print(sort(d))
