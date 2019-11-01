#import the random package so we can generate a randon AI choice
from random import randint

# "basket" of choices
choices=["rock", "paper", "scissors"]

# adding lives -> when one or the other gets to 0, win / lose
player_lives = 1
computer_lives = 1

# let the AI make a Choice
computer=choices [randint(0,2)]

# Set up a game loop here so we don't have to keep restarting
player = False

def winorlose(status):
	print("called win or lose", status)
	print("You", status, "! Would you like to play again?")
	choice = input("Y / N?")

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer
		#reset the game and start all over again
		player_lives = 1
		computer_lives = 1
		player = False
		computer = choices[randint(0, 2)]

	elif choice == "N" or choice == "n":
		print("You chose to quit. Better luck next time!")
		exit()
	else:
		print("Make a valid choice. Yes or no!")




while player is False:
	print("\n===============================")
	print("Computer Lives:", computer_lives, "/5")
	print("Player Lives:", player_lives, "/5")
	print("===============================")
	print("Choose your weapon!\n")
	player=input("choose rock, paper or scissors: \n")

	#start doing some logic and condition checking
	#print("\n computer: ", computer, "\n player: " , player )

	#always check a breaking condition first
	if player == computer:
		#we have a tie, no point in going any further
		print("\n tie, no one wins! try again \n")

	elif player == "quit":
		print("\n you chose to quit quitter. \n")
		exit()

	elif player == "rock":
		if computer == "paper":
			print("\n you lose!", computer, "covers", player, "\n")
			player_lives = player_lives -1
		else:
			print("\n you won!", player, "smashes", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "paper":
		if computer == "scissors":
			print("\n you lose!", computer, "cuts", player, "\n")
			player_lives = player_lives -1
		else:
			print("\n you won!", player, "covers", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "scissors":
		if computer == "rock":
			print("\n you lose!", computer, "smashes", player, "\n")
			player_lives = player_lives -1
		else:
			print("\n you won!", player, "cuts", computer, "\n")
			computer_lives = computer_lives -1

	if player_lives is 0:
		winorlose("lost")
		#print("You lost! Loser. Would you like to play again?")
		# choice = input("Y / N?")

		# if choice == "Y" or choice == "y":
		# 	#reset the game and start all over again
		# 	player_lives = 1
		# 	computer_lives = 1
		# 	player = False
		# 	computer = choices[randint(0, 2)]
		# elif choice == "N" or choice == "n":
		# 	print("You chose to quit. Better luck next time!")
		# 	exit()
		# else:
		# 	print("Make a valid choice. Yes or no!")
			
	elif computer_lives is 0:
		winorlose("won")
		#print("You won! Would you like to play again?")
		# choice = input("Y / N?")

		# if choice == "Y" or choice == "y":
		# 	#reset the game and start all over again
		# 	player_lives = 1
		# 	computer_lives = 1
		# 	player = False
		# 	computer = choices[randint(0, 2)]
		# elif choice == "N" or choice == "n":
		# 	print("You chose to quit. Better luck next time!")
		# 	exit()
		# else:
		# 	print("Make a valid choice. Yes or no!")
		# 	choice = input("Y / N?")

	else:
		player = False
		computer=choices[randint(0,2)]