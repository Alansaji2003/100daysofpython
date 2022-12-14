print('''
*******************************************************************************      
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______   
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("")
d=input("You are at a cross road, where do you want to go? Left or Right ")
d=d.lower()
if d=="right":
  print("")
  print("You see an old beggar by the side of the street")
  d=input("Will you give the beggar a coin? yes or no ")
  d=d.lower()
  if d=="yes":
    print("")
    print("You took a coin out of your pocket and gave it to the poor beggar. He took a dagger out of his robes and stabs you to death and steals your money. GAME OVER!! (try again generous lad)")
  else:
    print("")
    print("You pass the beggar man and falls into a hole, you reach a secret basement, the basement was full of gold and jewels!!! Then you wake up from your dream..... GAME OVER? yea try again sleepy head ")
else:
  print("")
  d=input("You see a lake, there is an island on the lake, are you waiting for the boat or going to swim? wait or swim ")
  d=d.lower()
  if d=="swim":
    print("")
    print("How could you choose something so obviously dangerous? what did you expect? mermaids? Ofcourse the sharks bit your head off.! GAME OVER!! Come back with new head lol")
  else:
    print("")
    d=input("You reach the island. You see a cave, inside the cave there is 3 doors. RED,BLUE and YELLOW, which door are you choosing? ")
    d=d.lower()
    if d=="red":
      print("")
      print("Well congradulations!!! your wife found out you have been cheeting with her for the past 3 years!! lol GAME OVER!")
    if d=="blue":
      print("")
      print("CONGRATS LAD!!!! you have succesfully completed the game but didnt get the treasure because while you were here wasting time, I stole your lover. Lol game over sucker!!")
    if d=="yellow":
      print("")
      print("maan yeah you got the treasure congrats now go and do something productive for godsakes!! just kidding you are the winner so you rule the world champ!! muah have a nice day!")
  
  




