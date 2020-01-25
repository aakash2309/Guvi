def add(a,b):
  sum=a+b
  print(sum)
def sub(c,d):
  sub=c-d
  print(sub)
def mul(e,f):
  mul=e*f
  print(mul)
def div(g,h):
  div=g/h
  print(div)
option=input("s to continue..")
while option!='q':
  print("1.add 2.sub 3.mul 4.div")
  choice=int(input("your choice is..."))
  x=int(input("enter 1st number:"))
  y=int(input("enter 2nd  number:"))
  if (choice==1):
     add(x,y)  
  elif (choice==2):
     sub(x,y)
  elif (choice==3):
     mul(x,y)
  else:
     div(x,y)
  option=input("enter s to continue or q to quit")
   
    

  


     
