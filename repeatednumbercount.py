from collections import Counter
s="hello by hello"
result = Counter(s)
print(result)
# b= list([item for item in result if result[item]>1])
# print(b)

l = [1,2,3,1,2,1,2,3,4,5,6,4,5]
k=[]
v=[]
for i in l:
    if i not in v:
        v.append(i)
    else:
        k.append(i)
print(v)       
print(k)