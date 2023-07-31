set={(5,6),(2,8),(5,0),(3,2),(6,5),(8,9),(2,3),(0,5)}
lst=[]
for (x,y) in set:
    if (y,x) in set:
       lst.append((x,y))
print(lst)

