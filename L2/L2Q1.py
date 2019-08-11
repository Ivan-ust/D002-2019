n = int(input("Please input a positive integer number larger than 2:\n"))
x = 3
if n <= 0 :
    print("It is not a prime number.")
while x <= n/2 :
    if n%x == 0 :
        print("It is not a prime number.")
        x = x + 1
        break
    else :
        x = x + 1
if n > 0 and x > n/2 :
    print("It is a prime number.")


    
