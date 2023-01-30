import random
import replit
from art import logo
print(logo)
print("Welcome to number guessing game!!")
choice = input("Want easy mode 🫠 ? or hard mode 🥵 ? Type easy or hard \n")
choice.lower()
cn = random.randint(1,100)
print(cn)
def check():
  global attempts
  global cn
  un = input("Guess a number between 1 and 100 ")
  
  while attempts > 0:
    if(int(un) > cn):
      print("Too high. Guess again")
      attempts -= 1
      print(f"You have {attempts} attempts left")
      check()
    elif(int(un) < cn):
      print("Too low. Guess again")
      attempts -= 1
      print(f"You have {attempts} attempts left")
      check()
    elif(int(un) == cn):
      print(f"Congragulations. The number was {cn}.")
      attempts = -1
      break
  if(attempts == 0):
    attempts = -1
if choice == "easy":
  attempts = 10;
  print("You have 10 attempts")
  check()
elif choice == "hard":
  attempts = 5;
  print("You have 5 attempts")
  check()
else:
  print("Please type 'easy' or 'hard', Run again.")


  