import random
print("=== Rock Paper Scissors Game ===")
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
while True:
    print("\nChoose: rock / paper / scissors")
    user_choice = input("Your choice: ").lower()
    if user_choice not in choices:
        print("Invalid choice! Try again.")
        continue
    computer_choice = random.choice(choices)
    print("Computer choice:", computer_choice)
    if user_choice == computer_choice:
        print("Result: It's a Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Result: You Win!")
        user_score += 1
    else:
        print("Result: You Lose!")
        computer_score += 1
    print("\nScore:")
    print("You:", user_score)
    print("Computer:", computer_score)
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        break
