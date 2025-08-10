import sys

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
def game_over():
    print("Game Over!")
    sys.exit()
print("Round 1")
a = input('You\'re at a crossroad,where do you want to go?\n"left" or "right":')
if a == "left":
    print("Go ahead!You pass this round")
else:
    game_over()

print("Round 2")

b = input('You\'re standing at the bank of the river,What do you want to do?\n"wait" for the boat or "Swim" across the river:')
if b == "wait":
    print("Yah!!you make it for the next round")
else:
    game_over()
    

print("Round 3")
c = input('You\'re standing in front of 3 different color doors,What do you wants to choose?\n"yellow" door or "Red" door or "Black" door:')
if c == "yellow":
    print("Congrats!You got the Treasure Box")
elif c == "black":
    print("Oh!This room is full of snake\nYou choose the wrong door")
    game_over()
else:
    print("Lol!This is a gate of hell")
    game_over()

print("Thank you for playing the game!")
print("Hope you enjoyed the game!")

