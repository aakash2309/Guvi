cp=int(input("enter the cost price:"))
sp=int(input("enter the selling price:"))
profit=sp-cp
loss=cp-sp
same=cp=sp
if sp>cp:
  print("amount is gain",profit)
elif sp<cp:
  print("amount is loss",loss)
else:
  print("no profit or loss",same)
