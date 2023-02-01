# s="hello by hello"
# a=len(s)
# count=0
# for i in range(a):
#     if s[i] != ' ':
#         count=count+1
# print(count)

s="hesdfghjkkegg"
cnt={}
for i in s:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1
print(cnt)

# by using cllection import method

from collections import Counter
s="hello by hello"
result = Counter(s)
print(result)
print(type(result))