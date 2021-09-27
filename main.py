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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice > 2:
  print("You entered invalid")
else:
  ascii_list = [rock,paper,scissors]
  print(ascii_list[user_choice])

  print("Computer chose:")
  comp_choice = random.randint(0,2)
  print(comp_choice)
  print(ascii_list[comp_choice])

  if user_choice == comp_choice:
    print("Try Again")
  else:
    if user_choice == 0:
      if comp_choice == 2:
        print("You win")
      else:
        print("You loose")
    elif user_choice == 1:
      if comp_choice == 0:
        print("You win")
      else:
        print("You loose")
    else:
      if comp_choice == 1:
        print("You win")
      else:
        print("You loose")

