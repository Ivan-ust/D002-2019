#L2 Q6: Banana Guessing game

#Step 1: Import necessary modules
import random
#Step 2: Welcome Message
print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid. The number is from 1 to 100.''')
#Step 3: Choose a random number between 1-100
n = random.randint(1,100)
print ("shhh, Dave hides %s bananas" % n)
# define a flag for found/not found and counter on how many trials
found = False
count = 0
#Step 4: Give three chances to the players 
while count < 3 :
    g = int(input())
    if g == n :
        found = True
        count = count + 1
    else :
        found == False
        count = count + 1
    

#Step 5: Display a message
    if g > n and g < 100 :
        print("guess too large")
    elif g < n and g > 0 :
        print("guess too small")
    elif g < 1 or g > 100 :
        print("guess out-of-range")

    if count == 3 :
        print("Game over.")
        break

    if found == True :
            print('You got the correct guess in %d trials' % count)
            print('Dave\'s banana are now all yours!')
            break
    else :
            print("You failed to find the number of bananas Dave hid! Try again next")

    
