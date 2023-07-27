'''a = [1,2,3,1,4,5,2]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            a.pop(j)
    print(a[i])'''

a = [1,2,3,1,4,5,2]
seen = []
for i in a:
    if i not in seen:
        seen.append(i)
    for j in seen:
        print(seen[j])