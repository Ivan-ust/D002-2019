def checker(sentence, letter):
    result = []
    for i in range(0,len(sentence)) :
        if letter in sentence[i] :
            result.append(i)   
    return print(result)
        
a = checker("Apple", "p") # a = [1, 2]
b = checker("Banana", "p") # b = []
c = checker("Cat", "a") # c = [1]
