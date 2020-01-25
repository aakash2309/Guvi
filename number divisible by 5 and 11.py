num=int(input("enter the number:"))
if num%5==0 and num%11==0:
  print("the number is divisible by 5 and 11",num)
elif num%5==0 and num%11!=0:
  print("the number is divisible by 5 but not div by 11",num)
else:
  print("the number is not div by both 5 and 11",num)

