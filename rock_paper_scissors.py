
import random

print("Welcome to Rock Paper Scissors!")

while True:
    user = input("\nEnter rock, paper, scissors (or quit): ").lower()

    if user == "quit":
        print("Thanks for playing!")
        break

    if user not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Try again!")
        continue

    computer = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif user == "rock" and computer == "scissors":
        print("You won!")
    elif user == "paper" and computer == "rock":
        print("You won!")
    elif user == "scissors" and computer == "paper":
        print("You won!")
    else:
        print("Computer won!")

print("Game ended.")
