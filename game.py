#import the random package so we can generate a randon AI choice
from random import randint

# "basket" of choices
choices=["rock", "paper", "scissors"]

# let the AI make a Choice
computer=choices [randint(0,2)]

# Set up a game loop here so we don't have to keep restarting
player = False

while player is False:
	player=input("choose rock, paper or scissors: \n")

	#start doing some logic and condition checking
	print("\n computer: ", computer, "\n player: " , player )

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
		else:
			print("\n you won!", player, "smashes", computer, "\n")

	elif player == "paper":
		if computer == "scissors":
			print("\n you lose!", computer, "cuts", player, "\n")
		else:
			print("\n you won!", player, "covers", computer, "\n")

	elif player == "scissors":
		if computer == "rock":
			print("\n you lose!", computer, "smashes", player, "\n")
		else:
			print("\n you won!", player, "cuts", computer, "\n")

	player = False
	computer=choices[randint(0,2)]