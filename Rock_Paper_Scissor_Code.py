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
#draw.io for flow chart
#ascii art for different type of art made from ascii.
import random
list_item = [rock,paper,scissors]
number= input("Welcome to the rock paper and scissors game.\n Choose 0 for Rock , 1 for Paper and 2 for Scissors.\n")
number_selected_by_user = int(number)
image = list_item[number_selected_by_user]
print("You:")
print(image)

random_number_for_computer = random.randint(0,2)
image2 = list_item[random_number_for_computer]
print("Computer:")
print(image2)

if random_number_for_computer >=3 and number_selected_by_user < 0 :
    print("Invalid Data")
elif  random_number_for_computer == 2 and number_selected_by_user == 0 :
    print("You Win")
elif  random_number_for_computer > number_selected_by_user :
    print("You Lose")
elif random_number_for_computer == number_selected_by_user :
    print("Draw")
elif random_number_for_computer == 0 and number_selected_by_user == 2 :
    print("You Lose")
elif random_number_for_computer < number_selected_by_user :
    print("You Win")
