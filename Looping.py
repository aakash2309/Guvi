#EVEN NUMBERS FROM 1 TO 100:
i=2
n=100
while i<=n:
  if i%2==0:
    print(i)
  i=i+1

 #ODD NUMBERS FROM 1 TO 100:
i=1
n=100
while i<=n:
  if i%2!=0:
    print(i)
  i=i+1
  
  #ALL NATURAL NUMBERS FROM 1 TO N:
n=int(input("enter any num:"))
i=1
while i<=n:
    print(i)
    i=i+1
    
 #ALL NATURAL NUMBERS FROM N TO 1:
n=int(input("enter any num:"))
i=n
while i>=1:
    print(i)
    i=i-1
    
 #ALPHABETS FROM A TO Z:
alpha={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
n=26
i=1
while i<=n:
   print(alpha[i])
   i=i+1
  
#SUM OF ALL EVEN NUMBERS FROM 1 TO N:
n=int(input("enter any num:"))
i=1
s=0
while i<=n:
  if i%2==0:
    s=s+i
  i=i+1
print(s)


#SUM OF ALL ODD NUMBERS FROM 1 TO 100:
n=int(input("enter any num:"))
i=1
s=0
while i<=n:
  if i%2!=0:
    s=s+i
  i=i+1
print(s)

#SUM OF ALL NATURAL NUMBERS FROM 1 TO N:
n=int(input("enter any num:"))
i=1
s=0
while i<=n:
    s=s+i
    i=i+1
print(s)











  
