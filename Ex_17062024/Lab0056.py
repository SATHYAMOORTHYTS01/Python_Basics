# *args - any number of arguments
from multiprocessing.forkserver import read_signed
from traceback import print_tb

print("salam")


def sum3(a=1,b=4,c=4):
    return a+b+c
result1 = sum3()
result2= sum3(a=2,b=4)
result3 = sum3(a=2, b=4, c=22)
print(result1,result2,result3) 


