a = ["A","E","I","O","U","a","e","i","o","u"]
list = []
n = 1
word = input("Please enter 10 words in total. Enter the first word now.\n")
while n < 10 :
    if word[0] in a :
        list.append(word)
    word = input("This is no.%d word. Next\n" % n)
    n = n + 1
print("This is no.10 word.")
print("Words start with a e i o u are",list)
