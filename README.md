# 100_Days_Python


Day 1-15
---------
leap year calculator    
scissors-paper-stone with ASCII art     
Strong password generator (use of list shuffles)      


Reebog's world
---------
![image](https://user-images.githubusercontent.com/87584870/180764397-3345ac4d-e305-4cfb-b1c5-7c5ea963700a.png)     
In this specific problem, using our previous version of the code. the robot will move in a infinite square loop, as shown below     
![image](https://user-images.githubusercontent.com/87584870/180764574-dea88eeb-100a-4127-b83b-3e09ea31f688.png)     
There are two ways to resolve this problem:
1. Using a counter.
    if right_is_clear() and counter <4: (why 4? it looks as tho the cycle 4 forms a square)   
    
2. The only reason why the infinite loop occurs is because the wall on the right IS NEVER present. We can also resolve this problem by making sure that there is ALWAYS A WALL ON THE RIGHT SIDE, before the main body of the code happens. This be done by:    
    1. while front_is_clear():   ##move till the robot hits a wall(WALL A)
             move()         
    2. turn_left()  ##there is now a wall present on the right side of the robot(YES this is WALL A)    
