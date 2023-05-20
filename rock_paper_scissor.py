import random
ls = ['rock','paper','scissor']
c = random.choice(ls)
v = input('choose rock/paper/scissor :')
if c == v:
    print('draw')
elif c>v:
    print('computer wins')
elif c<v:
    print("you win")
else:
    print('invalid')
