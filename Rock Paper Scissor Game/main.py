import random

chances = {'R':"Rock", 'P':"Paper", 'S':"Scissors"}
user_score = 0
computer_score = 0
user_count = 0
computer_count = 0
games = int(input(" How many games do you want to play?"))

while (user_count < games):

    user_choice = input("\nEnter your choice:") [0]
    user_choice = user_choice.upper()       # convert every letter upper case to make it valid
    user_count = user_count + 1
    computer_choice = random.choice(list(chances.keys()))
    print("You entered: ", chances[user_choice])
    print("Computer entered: ", chances[computer_choice])

    for i in chances:
        if (user_choice != i):
            print("Invalid choice")
            break

    if(user_choice =='R' and computer_choice == 'P') or (user_choice =='S' and computer_choice == 'P') or (user_choice =='R' and computer_choice == 'S'):
        user_score = user_score + 1
        print("User Won")
    elif (computer_choice == 'R' and user_choice == 'P') or (computer_choice == 'S' and user_choice == 'P') or (computer_choice == 'R' and user_choice == 'S'):
        computer_score = computer_score + 1
        print("Computer Won")
    else:
        print("Match TIE")

# After ending loop it will show total scores
print("\n\t\tFINAL SCORE:")
print("User Score:",user_score,"\t\t\tComputer Score:",computer_score,"\n")
if user_count>computer_count:
	print("\tCONGRATULATIONS! YOU WON!\n")
elif user_score<computer_score:
	print("\tSORRY! YOU LOST!\n")
else:
	print("\t\tOOPS! IT'S A TIE!\n")
