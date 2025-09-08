import random

keep_playing = True
computer_wins = 0
human_wins = 0
while keep_playing:
    
    answers = ["rock", "paper", "scissors"]
    computer_answer = random.choice(answers)
    print("do you wanna play rock, paper, scissors, or quit?")
    human_answer = input()
    human_answer = human_answer.lower()
    if human_answer == "quit":
        break

    if human_answer not in answers:
        print("that wasnt an option")
        exit()

    print(f"computer played {computer_answer}")

    if computer_answer == human_answer:
        print("nobody wins")

    elif computer_answer == "rock" and human_answer == "scissors":
        computer_wins += 1
        print("computer wins")
    elif computer_answer == "paper" and human_answer == "rock":
        computer_wins += 1
        print("computer wins")
    elif computer_answer == "scissors" and human_answer == "paper":
        computer_wins += 1 
        print("computer wins")
    else: 
        human_wins += 1
        print("human wins")
    print(f"human score {human_wins} computer score {computer_wins}")
print("thanks for playing <3")