game=input("Hi! welcome to quiz game..")
name=input("enter your name:\t")
age=input("enter your age:\t")
start=input("enter s to start the quiz game\t")
while start=='s':
  print("The Quiz game levels are..")
  print("select the level:")
  questions=['what is the color of sun?','what is the color of sky','what is sun made up of?','how many planets are there in solar system?','what is the name of sun?']
  leveltype=input("1.easy 2.medium 3.hard 4.very hard\n")
  if (leveltype=='1'):
     print(questions[0])
     ans=input("1.red 2.green 3.orange 4.white\n")
     if ans!='3':
       print(ans,"Sorry,your answer is wrong")
     else:
       print(ans,"Super!,your answer is correct")
       print(questions[2])
       ans2=input("1.liquid 2.solids 3.hotgas 4.gas\n")
       if ans2!='3':
        print(ans2,"sorry,wrong answer")
       else:
         print(ans2,"super!,correct answer")
         print("level successfully completed")
         q=input("do you want to quit?,press q..\t")
         if q=='q':
           break
         else:
          continue
  elif (leveltype=='2'):
     print(questions[1])
     ans1=input("1.black 2.blue 3.brown 4.red\n")
     if ans1!='2':
      print(ans1,"Sorry,your answer is wrong")
     else:
      print(ans1,"Super!,your answer is correct")
      print(questions[3])
      ans3=input("1.eight 2.nine 3.ten 4.seven\n")
      if ans3!='1':
        print(ans3,"sorry,wrong answer")
      else:
        print(ans3,"super!,correct answer")
        print("level successfully completed..")
        q=input("do you want to quit?,press q..\t")
        if q=='q':
          break
        else:
         continue
  elif leveltype=='3':
    print(questions[2])
    ans2=input("1.liquid 2.solids 3.hotgas 4.gas\n")
    if ans2!='3':
      print(ans2,"sorry,wrong answer")
    else:
      print(ans2,"super!,correct answer")
      print(questions[0])
      ans=input("1.red 2.green 3.orange 4.white\n")
      if ans!='3':
       print(ans,"Sorry,your answer is wrong")
      else:
       print(ans,"Super!,your answer is correct")
       print("level successfully completed..")
       q=input("do you want to quit?,press q...\t")
       if q=='q':
         break
       else:
         continue
  elif leveltype=='4':
    print(questions[3])
    ans3=input("1.eight 2.nine 3.ten 4.seven\n")
    if ans3!='1':
      print(ans3,"sorry,wrong answer")
    else:
      print(ans3,"super!,correct answer")
    print(questions[4])
    ans4=input("1.soe 2.sole 3.sow 4.sen\n")
    if ans4!='1':
      print(ans4,"sorry,wrong answer")
    else:
      print(ans4,"super!,correct answer")
      print("level successfully completed..")
      q=input("do you want to quit?,press q..\t")
      if q=='q':
         break
      else:
         continue
  else:
    print("choose the correct level type")
print("Thanks for playing..have a gud day.")

    
          


