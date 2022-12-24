from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
moreppl=True
bidders={}
while moreppl:
  n=input("What is your name? ")
  b=int(input("What is your bid?: $"))
  bidders[n]=b
  more=input("Are there any other bidders? Type 'yes' or 'no'")
  if more=="no":
    moreppl=False
  clear() 
high=0  
for i in bidders:
  bidamt=bidders[i]
  if bidamt>high:
    high=bidamt
    winner=i
 print(f"The winner {winner} is with a bid of ${high}")