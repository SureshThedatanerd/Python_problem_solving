a = [1,2,3,1,4,5,2,3,5,8]
seen = []
for i in a:
    if i not in seen:
        seen.append(i)
print(seen)
