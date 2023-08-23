import random


# returns first empty board
def first_blank(word):
    blank = ["_"] * len(word)
    space = word.find(" ")
    if space != -1:
        blank[space] = "-"
    return blank


# converts str to list
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


# returns updated board
def game_board(word, guess, blank):
    lst = Convert(word)  # declaring word as a list (lst)
    num = lst.count(guess)  # amount of times guess is in word (num)
    while num > 0:
        temp = lst.index(guess)  # first time guess occurs in lst
        lst[temp] = '~'  # changes the first occurence of guess to '-'
        blank.pop(temp)  # Removes:'_' at the position of temp(in blank)
        blank.insert(temp, guess)  # Adds guess at the position of temp(in blank)
        num = lst.count(guess)  # recalculates amount of times guess is in word
    return blank


def body(count):
    body1 = """\nwrong guess :(    
             ________
             |      o
             |        
             |       
             |      
            _|_\n"""

    body2 = """\nwrong guess again :(    
             ________
             |      o
             |      |  
             |      
             |     
            _|_\n"""

    body3 = """\nwrong guess again :(    
             ________
             |      o
             |      |  
             |      | 
             |      
            _|_\n"""

    body4 = """\nand again :(    
             ________
             |      o
             |     \|   
             |      | 
             |      
            _|_\n"""

    body5 = """\noh no! :(    
             ________
             |      o
             |     \|/   
             |      | 
             |      
            _|_\n"""
    body6 = """\nclose to the enddd :(    
             ________
             |      o
             |     \|/   
             |      | 
             |     /  
            _|_\n"""

    body7 = """\nyoure trash :(   
             ________
             |      o
             |     \|/   
             |      | 
             |     / \ 
            _|_\nYOU LOSE!"""

    if count == 1:
        return body1
    elif count == 2:
        return body2
    elif count == 3:
        return body3
    elif count == 4:
        return body4
    elif count == 5:
        return body5
    elif count == 6:
        return body6
    elif count == 7:
        return body7


def main():
    count = 0
    print("welcome to car brand hang-man, ready to play? here we go...\nGUESS THE CAR BRAND:")
    word_list = ["MERCEDES BENZ", "TESLA", "BMW", "ROLLS ROYCE", "BENTLEY", "BUGATTI", "PORSCHE", "LEXUS", "LAND ROVER",
                 "TOYOTA", "AUDI", "JAGUAR", "VOLVO", "VOLKSWAGEN", "JEEP", "FIAT", "FORD", "NISSAN", "HONDA",
                 "CHEVROLET", "LAMBORGHINI", "FERRARI", "SKODA", "HYUNDAI", "KIA", "MASERATI"]
    word = random.choice(word_list)
    blank = first_blank(word)
    print(blank)
    while count != 8:
        lower_guess = input("\nenter guess: ")
        guess = lower_guess.upper()
        if guess not in word:
            count = count + 1
            print(body(count))
            if count == 7:
                print("the car brand was: " + word)
                break
        blank = game_board(word, guess, blank)
        print(blank)
        if blank.count('_') == 0:
            print("YOU WIN!!! the car brand was: " + word)
            break
    print("good game!")


if __name__ == "__main__":
    main()
