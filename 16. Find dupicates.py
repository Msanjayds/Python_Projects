# Program to find duplicates in a List
def find_dups(x):
    length = len(x)
    dups  =[]
    for i in range(length):
        n = i + 1
        for a in range(n,length):
            if x[i] == x[a]:
                dups.append(x[i])
    return dups


x = ('a','b','a','c','a')

print(find_dups(x))