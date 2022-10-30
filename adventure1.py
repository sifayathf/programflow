available_exits = ["north", "south", "east", "west"]

chosen_exit=""
while chosen_exit not in available_exits:
    chosen_exit=input("Please chose a direction: ")
    if chosen_exit.casefold() =="quit":   # both ignores title case
        print("Game Over")
        break

print("aren't you glad you got out of there ")
