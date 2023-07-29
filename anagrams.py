str1=input("enter 1st string : ")
str2=input("enter 2nd string : ")
l1=len(str1)
l2=len(str2)
if l1==l2:
    l1=list(str1)
    l2=list(str2)
    l1.sort()
    l2.sort()
    if l1==l2:
         print("Anagrams")
    else:
      print("Not Anagrams")
else:
    print("Not Anagrams")

