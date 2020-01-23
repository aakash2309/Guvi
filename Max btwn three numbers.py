a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
c=int(input("enter the number3:"))
if a>b and a>c:
  print("A is greater",a)
elif b>a and b>c:
  print("B is greater",b)
elif a==b==c:
  print("All are equal",c)
else:
  print("C is greater",c)

