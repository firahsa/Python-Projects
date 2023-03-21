name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

anwser = input(
    "You are at a crossroads and you must choose to go on the right path or the left path. Which path do you choose? ").lower()

if anwser == "right": 
    anwser = input(
        "You come to a beautiful, quiet forest clearing. You can go straight-ahead onto the path or get your map out. Type walk to walk or map to get map out: ")

    if anwser == "walk":
        print("You walked for a mile and ended up getting lost. You lost the game. ")
    elif anwser == "map":
        print("You followed the map in your bag, but it was faulty so you ended up getting lost. You lost the game. ")
    else:
        print("Not a valid option. You lose. ")

elif anwser == "left":
    anwser = input(
        "You come to a nice river, it looks gentle. Do you swim across it or create a makeshift boat with the resources around you. Do you swim or create makeshift boat (swim/boat)? ")

    if anwser == "swim":
        print("You swim across the river and got eaten by an alligator. You lost the game.") 
    elif anwser == "boat":
        anwser = input(
            "You made a makeshift boat with the little resources you had and successfully crossed the river. You come across a stranger. Do you talk to them (yes/no) ? : ")

        if anwser == "yes":
            print("You talk to the stranger and he gives you valuable information and gold to continue in the game. You win!")
        elif anwser == "no":
             print("You ignore the stranger and they are offended and you get lost. You lose the game.") 
        else:
             print("Not a valid option. You lose.")
    
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying this game", name)