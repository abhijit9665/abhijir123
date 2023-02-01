# s=121
# r=str(s)
# for i in len(s):
#     for j in 
#     if r[i]<r[j]:
#         print('true')
# else:
#     print('False')

def is_sorted(number):
    num_list = [int(i) for i in str(number)]
    if num_list == sorted(num_list):
        return True
    elif num_list == sorted(num_list, reverse=True):
        return False
    else:
        return "The Number is not sorted"
n = int(input("enter a integer number : - "))
s=is_sorted(n)
if s == True:
    print("the number is increasing order ")
elif s == False:
    print("the number is decresing order ")
else:
    print("this is not increasing and decreasing order")