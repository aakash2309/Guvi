def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
ch='y'
f=open("calc.txt","w+")
while ch=='y':
    c=int(input("enter your choice 1.add 2.sub 3.mul 4.div:\n"))
    if c==1:
        a=int(input())
        b=int(input())
        d=add(a,b)
        f.write("Number 1 is %d\n"%a)
        f.write("Number 2 is %d\n" %b)
        f.write("add of two num is %d\n"%d)
    elif c==2:
        a=int(input())
        b=int(input())
        s=sub(a,b)
        f.write("Number 1 is %d\n" % a)
        f.write("Number 2 is %d\n" % b)
        f.write("sub of two num is %d\n"%s)
    elif c==3:
        a=int(input())
        b=int(input())
        m=mul(a,b)
        f.write("Number 1 is %d\n" % a)
        f.write("Number 2 is %d\n" % b)
        f.write("mul of two num is %d\n"%m)
    elif c==4:
        a=int(input())
        b=int(input())
        d=div(a,b)
        f.write("Number 1 is %d\n" % a)
        f.write("Number 2 is %d\n" % b)
        f.write("div of two num is %d\n"%d)
    else:
        f.write("wrong choice")
    ch=input("y to continue...")
    f.write("choices:%s\n"%ch)
f.close()
f=open("calc.txt","r+")
print(f.read())
f.close()

