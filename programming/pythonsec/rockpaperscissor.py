import random

print("WELCOME TO ROCK PAPER SCISSORS GAME")
print("Rules of the Game")
print ("rock vs scissors ->  Rock Wins")
print("Paper vs scissors ->  Scissors Wins")
print ("paper vs rock  -> Paper Wins")

choices = ["Rock" , "Paper" , "Scissors"]

while True:
    print("Choose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    # To validate the user's input 

    try:
        choice = int(input("Enter Your Choose :"))
    except ValueError:
        print("ENTER A VALID CHOICE")
        continue
    if choice < 1 or choice > 3:
        print ("Please enter a valid choice from 1 -3")
        continue
        

    user_choice = choices[choice - 1]
    print ("Your choice is :", user_choice)

# To get computers choice
    print("Its now computers turn.....")
    computer_turn = random.randint(1,3)
    comp_choice = choices[computer_turn - 1]

    print("The computers choice is: ", comp_choice)
    print(user_choice, "vs", comp_choice)

    # To determine the winner
    if choice == computer_turn:
        print("NO one wins its a tie!!!")
    elif(
        (choice == 2 and computer_turn == 1 ) or 
        (choice == 3 and computer_turn == 2) or
        (choice == 1 and computer_turn == 3) 
    ):    
        print ( "<======YOU WIN HAHA!!!======>")
    else:
        print("THE COMPUTER WINS!!!LOOSER HAAAAAAA!!")    


    # To enable the user to play again
    while True:
        ans = input("Do You Want To Play This Game Again? (Y / N): ").lower()

        if  ans in ['y', 'n']:

            break

    if ans == 'n':
            break
    print ()
print("/n =======Thanks for playing the game . Hope you enjoyed it====== ")        
        



