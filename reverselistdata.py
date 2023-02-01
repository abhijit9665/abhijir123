l = ['abhijit',57,'data']

def reverse_list(l):
    l1=[]
    for i in l:
        if isinstance(i ,str):
            l1.append(i[::-1])
        else:
            l1.append(i)
    return l1[::-1]

print(reverse_list(l))