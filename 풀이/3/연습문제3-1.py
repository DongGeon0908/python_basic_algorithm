name = ["Tom","Jerry","Mike"]
n = len(name)

for i in range(0, n-1):
    for j in range(i+1, n):
        if name[i] != name[j]:
            print(name[i] + "-" +name[j])


