yr = int(input("Input the year\n"))
if yr%4 == 0 and yr%100 != 0 :
  print("Yes, it is a leap year")
elif yr%400 == 0 :
  print("Yes, it is a leap year")
else : print("No, it is not a leap year")  
