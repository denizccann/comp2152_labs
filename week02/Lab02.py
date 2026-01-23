# Solution to Week 02 questions
import random 

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter your choice (1-Rock, 2-Paper, 3-Scissors):")
playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Invalid choice!")
else:
    computerChoice = random.randint(1, 3)

if playerChoice == computerChoice:
    print("It's a tie!")
elif playerChoice == 1 and computerChoice == 3:
print("Rock beats scissors - you win!")
elif playerChoice == 2 and computerChoice == 1:
print("Paper beats Rock - you win!")
elif playerChoice == 3 and computerChoice == 2:
    print("Scissors beats Paper - You win!")