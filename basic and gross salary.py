bs=int(input("enter the basic salary:"))
if bs<=1000:
  h=bs*0.2
  d=bs*0.8
  gs=h+d+bs
  print("gross salary is:",gs)
elif bs<=2000:
  h=bs*0.25
  d=bs*0.9
  gs=h+d+bs
  print("gross salary is:",gs)
elif bs>2000:
  h=bs*0.3
  d=bs*0.95
  gs=h+d+bs
  print("gross salary is:",gs)


      





