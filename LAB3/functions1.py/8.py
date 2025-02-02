def spy_game(numbers):
     for i in range(len(numbers)-1):#Это делается потому, что мы сравниваем два соседних элемента
        if(numbers[i]==numbers[i+1]==0 and numbers[i+2]==7):
            return True
     return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

