def search_list(a, x):
    n = len(a)
    for i in range(0,n):
        if x == a[i]:
            return i
    return -1

v = [1,2,3,4,5,20,4,6,7]
print(search_list(v, 20))
