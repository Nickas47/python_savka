"""Python: Lab9.1(Moduls)
Mykola Boiko, pm- 12343"""
def GuessNumber():
    from random import randint
    randNumber = randint(0,10)
    userNumber = int(input('Your number = '))
    if randNumber == userNumber:
        print('Victory!!!')
    else:
        print('The right number was {}. Try again'.format(randNumber))
        
if __name__ == "__main__":    
    GuessNumber()




