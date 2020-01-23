char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digit=['0','1','2','3','4','5','6','7','8','9','10']
special=['!','@','#','$','%','^','&','*','(',')','_']
ch=input("enter any alphabet:")
if ch in char:
    print("the given character is an alphabet")
elif ch in digit:
    print("the given character is a digit")
else:
   print("the given character is a special character")
    
    
    
    
