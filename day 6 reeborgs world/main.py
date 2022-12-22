def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    i=0
    while i<=4: #to count the infinite loop
        
        if right_is_clear():
           
            turn_right()
            move()
            i+=1
        elif front_is_clear():
            
            move()
            
        else:
            turn_left()
            i=5
  
    if front_is_clear():
        
        move()    
    else:
        turn_left()
                   
        
  
              
    

