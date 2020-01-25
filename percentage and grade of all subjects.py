s1=int(input("enter the marks for physics sub:"))
s2=int(input("enter the marks for chemistry sub:"))
s3=int(input("enter the marks for biology sub:"))
s4=int(input("enter the marks for maths sub:"))
s5=int(input("enter the marks for computer sub:"))
total=s1+s2+s3+s4+s5
percentage=float((total/500)*100)
if percentage>=90:
  print("Grade A")
elif percentage>=80:
  print("Grade B")
elif percentage>=70:
  print("Grade C")
elif percentage>=60:
  print("Grade D")
elif percentage>=40:
  print("Grade E")
elif percentage<40:
  print("Grade F")
else:
  print("fail")


      





