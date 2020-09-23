def search_list(a, x):
    n = len(a)
    for i in range(0,n):
        if x == a[i]:
            return i
    return "?"

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

if search_list(stu_no, 14) == "?":
    print("?")
else:
    print(stu_no[search_list(stu_no, 14)])
