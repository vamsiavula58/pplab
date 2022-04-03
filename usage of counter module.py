from collections import Counter
n=int(input("enter the number of items to be inserted"))
items=[]
for i in range(n):
    items.append(int(input("enter a items to be inserted")))
d=Counter(items)#returns a dictionary increasing order of their frequency
d=list(d)
print("the maximum frequent item is {} and minimum frequent item is {}".format(d[0],d[-1]))

