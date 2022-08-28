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

#Write your code below this line 👇
game_images = [rock, paper, scissors]

rock_paper_scissors = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
if rock_paper_scissors >= 3 or rock_paper_scissors < 0:
  print("You typed an invalid number, you lose!")
else:
 print(game_images[rock_paper_scissors])
 computer_choice = random.randint(0,2)
 print ("Computer choose")
 print(game_images[computer_choice])


# *************************************
  #Another method 

  
# if rock_paper_scissors == 0:
#   print(rock)
# elif rock_paper_scissors == 1:
#   print(paper)
# else:
#   print(scissors)

# if computer_choice == 0:
#   print(rock)
# elif computer_choice == 1:
#   print(paper)
# else:
#   print(scissors)
# ****************************************




 if rock_paper_scissors == 0 and computer_choice == 2:
    print("You win!")
 elif computer_choice == 0 and rock_paper_scissors == 2:
    print("You lose!")
 elif computer_choice > rock_paper_scissors:
    print("You lose!")
 elif rock_paper_scissors > computer_choice:
    print("You win!")
 elif rock_paper_scissors == computer_choice:
    print("It's a Draw")
