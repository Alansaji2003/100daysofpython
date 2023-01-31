import random
from art import logo
from art import vs
from game_data import data
from replit import clear

# def morefame(a,b):
#   if a>b:
#     return a
#   else:
#     return b

def compare():
  rn = random.randint(0,49)
  rnn = random.randint(0,49)
  gameover = False
  nice =""
  score = 0;
  while(gameover == False):
    print(logo)
    print(nice +str(score))
    print("Compare A: "+ data[rn]['name'] + ", a " +  data[rn]['description']+ ", from " + data[rn]['country']+".")
    print(vs)
    print("Against B: "+ data[rnn]['name'] + ", a " +  data[rnn]['description']+ ", from " + data[rnn]['country']+ "." )
    choice = input("Who has more followers on instagram? Type 'A' or 'B'. ")
    choice.lower()
    if(choice == "a" and data[rn]['follower_count'] > data[rnn]['follower_count']):
      score +=1
      nice = "You are right! current score is:"
      rn = rnn
      rnn = random.randint(0,49)
      clear()
    elif(choice == "b" and data[rnn]['follower_count'] > data[rn]['follower_count']): 
      score +=1
      nice = "You are right! current score is:"
      rn = rnn
      rnn = random.randint(0,49)
      clear()
    else:
      clear()
      gameover = True
      print(f"Sorry You were wrong...  score: {score}")

compare()