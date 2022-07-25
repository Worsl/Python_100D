def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_around()
    turn_left()

count = 0
while at_goal() != True:

    if right_is_clear() and count < 4:
        turn_right()
        move()
        count += 1
    elif front_is_clear():
        move()
        count = 0
    else:
        turn_left()
        count = 0
