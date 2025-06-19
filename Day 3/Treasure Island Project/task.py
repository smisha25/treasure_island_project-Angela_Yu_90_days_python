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
start = input('You\'re at a crossroad. Where do you want to go?\n ."Left" or "Right"?\n').lower()


if start == "left":
    print("Congratulations! You've crossed the forest. There is now a lake in front of you")
    level_second = input('Type "wait" to wait for a boat. Type "walk"" to walk across\n').lower()
    if level_second == "walk":
        print(
            "Good Job! You have now crossed the lake and arrived at the island. \n" + "There is a house with three doors")
        final_round = input("One Red, one yellow and one blue. Which one do you choose?.\n").lower()
        if final_round == "red":
            print("Oh no! the fire caught you :(")
        elif final_round == "blue":
            print("CONGRATULATIONS! You have found the TREASURE!!!")
        elif final_round == "yellow":
            print("You have been caught by the beast. GAME OVER!!")
        else:
            print("You have chosen the wrong option. GAME OVER")

    else:
        print("Yikes! your boat had a hole. \n  GAME OVER.")
else:
    print("Oh no! You fell into a pit.")







