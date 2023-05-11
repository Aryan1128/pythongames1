import random as rd
def OTP(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return rd.randint(range_start, range_end)
def start():
    print("-"*(5))
    ch=input("Numeric  OPT N :").upper()
    if ch=='N':
        numOTP()
    else:
        print("Invalid Input")
def numOTP():
    print("-"*(5))
    n=int(input("enter no of digit of OTP:"))
    print(OTP(n))
print("OTP Genrator".center(100," "))
print(("-"*(5)).center(100," "))
start()
