# Rock Paper Scissor using concepts learned earlier
from random import randint
comp = "rps"
comp_choice = comp[randint(0,2)]
comp_choice2 = ""
if comp_choice == "r":
    comp_choice2 = "rock"
elif comp_choice == "p":
    comp_choice2 = "paper"
elif comp_choice == "s":
    comp_choice2 = "scissor"
user_choice = input("Choose Rock, Paper, Scissor (R,P,S): ").lower()
if user_choice == comp_choice:
    print(f"You and Comp both choose {user_choice}. Hence its a DRAW!! 😬")
elif (user_choice == "p" and comp_choice == "r") or (user_choice == "r" and comp_choice == "s") or (user_choice == "s" and comp_choice == "p"):
    print(f"Computer choose {comp_choice2}, You WON!! 🥳")
else:
    print(f"Computer choose {comp_choice2}, You LOST!! 😭")
