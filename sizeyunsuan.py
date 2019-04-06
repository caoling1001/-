import random
def shuru():
    a=str(random.randint(1,100))
    b=random.choice('+-*/')
    c=str(random.randint(1,100))
    d=random.choice('+-*/')
    e=str(random.randint(1,100))
    return a+b+c+d+e
def panduan():
    t=shuru()
    while True:
        if eval(t)<100:
            if eval(t)>0:
                return t
        t=shuru()
x=[]
with open('ss.txt','w+') as f:
    for i in range(30):
        t=panduan()
        while True:
            if t in x:
                t=panduan()
            else:
                x.append(t)
                break
        print(t)
        print(eval(t))
        f.write(t+'\n')
        