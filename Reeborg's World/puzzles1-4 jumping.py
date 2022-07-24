def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_around()
    turn_left()

def jump():
    height_count = 0
    turn_left()
    while not right_is_clear(): 
        move()
        height_count += 1
        
    turn_right()
    move()
    turn_right()
    
    while height_count != 0:
        move()
        height_count -= 1
    turn_left()
    
while at_goal() !=True:
    if wall_in_front():
        jump()
    else:
        move()
