
print("Welcome to the tip calculator")
total_bill=int(input("What was the total bill? Rs "))
prc_tip=int(input("What percentage tip would you like to give? 10,12 or 15 "))
people=int(input("How many people to split the bill "))
result=round(((total_bill*prc_tip/100)+total_bill)/people,2)
#to make the result have 2 decimal place no matter what
result="{:.2f}".format(result)
print(f"Each person should pay {result} Rs")