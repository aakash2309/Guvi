year=int(input("enter the year:"))
if year%4==0:
    print(year,"the year is a leap year")
elif year%400==0:
    print(year,"the year is a leap year")
elif year%100==0:
    print(year,"the year is not a leap year")
else:
    print(year,"the year is not a leap year")
    
