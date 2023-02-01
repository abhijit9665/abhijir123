
# def mul(a,b):
#     print(a,b)
#     if a == None:
#         print("input is none")
#     else:
#          print(a*b)

# # def f1(mul):
# #     a=f1(a,b)
# #     print(a)
        
# a=eval(input("input"))
# b=eval(input("second"))
# mul(a,b)
def decor(main_fun):
    var=main_fun()
    add=var+500
    print(add)
#@decor
def main_fun():
    return 500
decor(main_fun)
# result=main_fun()
# print(result)
