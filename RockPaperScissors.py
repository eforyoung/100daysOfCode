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
anything = '''
            ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'    
'''
game_images = [rock,paper,scissors,anything]
rps_play = int(input("What do you choose,type 0 for rock,1 for paper,2 for scissors? \n"))

computer_choice = random.randint(0,2)



print(game_images[rps_play])
print("The computer choose:")
print(game_images[computer_choice])

if rps_play == 0 and computer_choice == 1:
    print("The Game is Over,the system wins")
elif rps_play == 0 and computer_choice == 2:
    print("We have defeated the system")
elif rps_play == 0 and computer_choice == 0:
    print("It is a draw")
elif computer_choice == 0 and rps_play == 1:
    print("We have defeated the system")
elif computer_choice == 0 and rps_play == 2:
    print("The Game is Over,the system wins")
else:
    print("The number you choose is invalid so you need to keep your numbers within the range")
