import random
import time
print('Wining rules for the rock , paper , sessior game are :\n'
      +'Rock vs paper -> paper win \n'
      +"Rock vs scissor -> Rock win \n"
      +"paper vs scissor -> scissor win \n")

while True :
    print("Enter Your choice : \n 1-Rock \n 2-paper \n 3-scissor")

    choice= int (input("Enter Your choice :"))

    while choice >3 or choice <1:
        choice=int(input("Please enter a valid choice please :"))

    if choice == 1:
        choice_name = 'Rock '
    elif choice==2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    print("user choice is:\b", choice_name)
   # time.process_time_ns(5)
    print("Now its Computer Turn :\n")

    computer_choice = random.randint(1,3)

    if computer_choice == 1:
        comp_choice_name = 'rocK'
    elif computer_choice == 2:
        comp_choice_name = 'papeR'
    else:
        comp_choice_name = 'scissoR'
    print("Computer choice is :\b", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    if choice == computer_choice:
        print('Its a Draw', end="")
        result = "DRAW"

    if (choice == 1 and computer_choice == 2):
        print('paper wins =>', end="")
        result = 'papeR'
    elif (choice == 2 and computer_choice == 1):
        print('paper wins =>', end="")
        result = 'Paper'
        if (choice == 1 and computer_choice == 3):
            print('Rock wins =>\n', end="")
            result = 'Rock'
        elif (choice == 3 and computer_choice == 1):
            print('Rock wins =>\n', end="")
            result = 'rocK'

        if (choice == 2 and computer_choice == 3):
            print('Scissors wins =>', end="")
            result = 'scissoR'
        elif (choice == 3 and computer_choice == 2):
            print('Scissors wins =>', end="")
            result = 'Rock'
            # Printing either user or computer wins or draw
        if result == 'DRAW':
            print("<== Its a tie ==>")
        if result == choice_name:
            print("<== User wins ==>")
        else:
            print("<== Computer wins ==>")
        print("Do you want to play again? (Y/N)")
        ans = input().lower
        if ans =='n':
            break
        print("Thanks for Playing ..............")

