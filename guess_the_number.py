import random as rd
att = 10
a=rd.randint(1,50)
while att>0:
    n = int(input('enter the between 1 to 50 number'))
    if n>a:
        print("Guess the Lower")
    elif n<a:
        print('guess the higher')
    elif n==a:
        print('you did it')
        att=1
