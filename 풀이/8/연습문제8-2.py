def select_sort(a):
    n = len(a)
    for i in range(0, n - 1):
        max = i
        for j in range(i + 1, n):
            if a[j] > a[max]:
                max = j
        a[i], a[max] = a[max], a[i]


d = [2, 4, 5, 1, 3]
select_sort(d)
print(d)
