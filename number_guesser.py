import random

number = random.randint(1,100)
attempts = 0

while attempts < 5:
    try:
        guess = int(input("Guess a number between 1 to 100: "))
        
        if guess == number:
            print("you got it!")
            break
        elif guess < number:
            print("too low, try again!")
        else:
            print("too high, try again!")
            
        attempts += 1
        print("attempts left:", 5 - attempts)
        
    except:
        print("Invalid input! Try again.")
    
print("Game over. The number was", number)