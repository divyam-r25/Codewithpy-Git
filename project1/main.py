import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
'''
1 for rock
-1 for paper
0 for scissor '''

computer = random.choice([-1, 0, 1])
youstr = input("enter ur choice (r for rock, p for paper, s for scissors): ").lower()
youDict = {"s": 1, "p": -1, "r": 0}
reverseDict = {1: "s", -1: "p", 0: "r"}
if youstr not in youDict:
    print("Invalid input! Please enter 'r', 'p', or 's'.")
    exit()
you = youDict[youstr]

print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == -1 and you == 1):
    print("you win")
    print("congrats!")
elif (computer == -1 and you == 0):
    print("you lost")
elif (computer == 0 and you == -1):
    print("you win")
    print("congrats!")
elif (computer == 0 and you == 1):
    print("you lost")
elif (computer == 1 and you == 0):
    print("you win")
    print("congrats!")
elif (computer == 1 and you == -1):
    print("you lost")

else:
    print("draw!")

# below method can replace with above if-elif lines .  ezzy!
'''

if ((computer - you) == -1 or (computer - you) == 2):
    print("you lose!")
elif ((computer - you) == 1 or (computer - you) == -2):
    print("you won!")
else:
    print("its a draw!")
'''





