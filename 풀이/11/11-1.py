def quick(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[-1]
    g1 = []
    g2 = []
    for i in range(0, n-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
    return quick(g1) + [pivot] + quick(g2)

d= [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick(d))
