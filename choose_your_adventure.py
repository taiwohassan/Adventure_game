name = input("Type your name:..")
print("Welcome ", name, " to this adventure!")

answer = input("You are in a dense forest, and the path splits into two. You can go left into the darker woods or right towards the sunny clearing. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You find yourself in a dark, eerie forest. You hear strange noises. Do you investigate or run back? Type 'investigate' to look around or 'run' to go back: ").lower()
    if answer == "investigate":
        print("You discover a hidden treasure chest filled with gold! You're rich!")
    elif answer == "run":
        print("You tripped while running, fell into a pit, and got stuck. You lose!")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You reach a sunny meadow with a mysterious cottage. Do you knock on the door or explore the meadow? Type 'knock' to approach the cottage or 'explore' to look around the meadow: ").lower()
    if answer == "knock":
        print("A friendly old woman offers you food and shelter. You win!")
    elif answer == "explore":
        print("You find a hidden tunnel leading to an underground maze, but you get lost and can't find your way out. You lose!")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")
