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

#1st way of doing it
game_choice = [rock , paper , scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)


final_round = random.randint(0,2)
print("Computer chose")
print(game_choice[final_round])

if choice > 2 or choice < 0:
    print("you chose an invalid option")
elif choice == 0 and final_round == 1:
    print("you loose")
elif choice == 0 and final_round == 2:
    print("you win")
elif choice < final_round:
    print("you loose")
elif choice > final_round:
    print("you win")
elif choice == final_round:
    print("it's a draw")



#2nd way of doing it
pics = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_choice < 0 or your_choice > 2:
    print("Don\'t enter numbers out of scope!'")
    exit()

print(pics[your_choice])

comp_choice = random.randint(0, 2)
print(f"Computer chose:\n{pics[comp_choice]}")

choice_matrix = [["It\'s a draw", "You lose", "You win"], ["You win", "It\'s a draw", "You lose"],
                 ["You lose", "You win", "It\'s a draw"]]
print(choice_matrix[your_choice][comp_choice])



