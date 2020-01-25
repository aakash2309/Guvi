a1=int(input("enter the 1st angle of a triangle:"))
a2=int(input("enter the 2nd angle of a triangle:"))
a3=int(input("enter the 3rd angle of a triangle:"))
s=a1+a2+a3
if s==180:
  print("valid triangle")
else:
  print("invalid triangle")
