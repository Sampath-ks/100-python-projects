import random
def guess_number():
    secret_number=random.randint(1,100)
    guess=None
    attempts=0
    print("Welcome to guess the number game")
    print("I'm thinking of a number between 1 to 100")
    while guess!=secret_number:
         try:
             guess=int(input("Enter number 1 to 100:"))
             attempts+=1
             if guess>secret_number:
              print("Too high!")
             elif guess<secret_number:
              print("Too low!")
             else:
                print(f"Correct! you guessed in {attempts} attempts")
         except ValueError:
             print("Invalid input,try numbers between 1 to 100")
guess_number()