'''
Project Name: Turtle race
Author: Aayush Kurup
Libraries used: turtle, random.randint, time.sleep
Start Date: 12-08-2018
Completion date: 12-08-2018
'''

import turtle
from random import randint
from time import sleep

def draw_track(turtle_main):    # this function will draw the race track
    for i in range(22):
        turtle_main.pd()
        turtle_main.forward(10)
        turtle_main.pu()
        turtle_main.forward(10)
        turtle_main.up()

def set_race(turtle_main):  # this function will draw the race start and end line
    turtle_main.penup()     # along with the separate tracks for each turtle
    turtle_main.setpos(-200,100)    # Width of the racetrack is 400 units
    turtle_main.right(90)
    turtle_main.pd()
    turtle_main.forward(200)
    turtle_main.pu()
    turtle_main.setpos(200,100)
    turtle_main.pd()
    turtle_main.forward(200)
    turtle_main.up()
    turtle_main.setpos(-210,50)
    turtle_main.left(90)
    draw_track(turtle_main)
    turtle_main.setpos(-210,0)
    draw_track(turtle_main)
    turtle_main.setpos(-210,-50)
    draw_track(turtle_main)
    turtle_main.ht()

'''
The below function will initialize all the players/turtles ,
set their shape and value
and return the instance of those players/turtles
'''
def set_players():

    player_1 = turtle.Turtle()   # defining player 1      
    player_1.shape('turtle')
    player_1.color('red')
    player_1.up()
    player_1.setpos(-220,75)
    player_1.pd()

    player_2 = turtle.Turtle()  # defining player 2
    player_2.shape('turtle')
    player_2.color('green')
    player_2.up()
    player_2.setpos(-220,25)
    player_2.pd()

    player_3 = turtle.Turtle()  # defining player 3
    player_3.shape('turtle')
    player_3.color('yellow')
    player_3.up()
    player_3.setpos(-220,-25)
    player_3.pd()

    player_4 = turtle.Turtle()  # defining player 4
    player_4.shape('turtle')
    player_4.color('blue')
    player_4.up()
    player_4.setpos(-220,-75)
    player_4.pd()

    return (player_1,player_2,player_3,player_4)    # return instance of each player

'''
the below function will start the race
'''
def start_race(turtle_main):
    
    player_1,player_2,player_3,player_4 = set_players()     # init Players
    flag = 1        # this flag will check if we have a winner or not

    '''
    the below loop will continue until all players reach the end line i.e x-cordinate=200
    '''
    while(player_1.xcor()<200 or player_2.xcor()<200 or player_3.xcor()<200 or player_4.xcor()<200):

        if(player_1.xcor()<200):    # if the player has not reached the end line
            player_1.forward(randint(1,10))     # move it some random unit forward in each iteration

        if(player_2.xcor()<200):    # if the player has not reached the end line
            player_2.forward(randint(1,10))     # move it some random unit forward in each iteration

        if(player_3.xcor()<200):    # if the player has not reached the end line
            player_3.forward(randint(1,10))     # move it some random unit forward in each iteration

        if(player_4.xcor()<200):    # if the player has not reached the end line
            player_4.forward(randint(1,10))     # move it some random unit forward in each iteration

        if(flag):   # if we have a winner
            
            if(player_1.xcor()>=200):  # if player 1 is the winner
                '''
                Then display player 1 wins and set flag = 0 (don't check for winner again)
                '''
                turtle_main.undo()
                turtle_main.write('Player 1 wins',align='center',font=("Arial", 20, "normal"))
                flag = 0

            elif(player_2.xcor()>=200): # if player 2 is the winner
                '''
                Then display player 2 wins and set flag = 0 (don't check for winner again)
                '''
                turtle_main.undo()
                turtle_main.write('Player 2 wins',align='center',font=("Arial", 20, "normal"))
                flag = 0
            
            elif(player_3.xcor()>=200):   # if player 3 is the winner
                '''
                Then display player 3 wins and set flag = 0 (don't check for winner again)
                '''
                turtle_main.undo()
                turtle_main.write('Player 3 wins',align='center',font=("Arial", 20, "normal"))
                flag = 0    
            
            elif(player_4.xcor()>=200):     # if player 4 is the winner
                '''
                Then display player 4 wins and set flag = 0 (don't check for winner again)
                '''
                turtle_main.undo()
                turtle_main.write('Player 4 wins',align='center',font=("Arial", 20, "normal"))
                flag = 0



'''
A timer is implemented in the below function
The race will start after 3 seconds
'''
def timer(turtle_main):
    for i in reversed(range(3)):
        turtle_main.write('The race will start in {}'.format(i+1),align='center',font=("Arial", 20, "normal"))
        sleep(1)
        turtle_main.undo()

'''
The function will display text 'Turtle Race' in the position (0,150)
'''
def display_turtle_race(turtle_main):
    turtle_main.pu()        
    turtle_main.setpos(0,150)
    turtle_main.write('Turtle Race',align='center',font=("Arial", 20, "bold"))


'''
The main function to execute the program
'''
def main():
    
    turtle_main = turtle.Turtle()       # the main turtle that willl draw the race track
    scr = turtle.Screen()           # Instance of the screen
    scr.title('Turtle Race')

    display_turtle_race(turtle_main)
    
    set_race(turtle_main) # this function will draw the race track
    turtle_main.setpos(0,-250) # this statement will set the main turtle at position (0,-250)

    timer(turtle_main)
    turtle_main.write('Let\'s go',align='center',font=("Arial", 20, "normal"))
    start_race(turtle_main)  # this function will start the race
    turtle.exitonclick()    # when the race ends the clicking the screen will close the window

'''
The main function will not execute if the file is imported
'''
if __name__ == '__main__':
    main()
