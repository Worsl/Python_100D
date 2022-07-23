year = int(input("Which year do you want to check? "))

if (year%4 != 0):
  print("not leap")

elif (year%4 == 0):
  if (year%100 !=0 ):
    print("Leap")

  elif (year%100 == 0):
    if (year%400 == 0):
      print("Leap")
    elif (year%400 !=0):
      print("Not leap")
    
    
  

