# Heath Hilton
# 11/13/2022

# Program: M03 Lab: List, Functions, and Classes

# A program to be an example for Super Classes.

#7.4 Make a list
things = ["mozzarella", "cinderella", "salmonella"]

#7.5 Capitalize the person and print out the list
things[1] = things[1].capitalize()
print(things)
#The word is now capitalized in the list.

#7.6 Capitalize the cheesey and print the list again
things[0] = things[0].upper()
things[2] = things[2].upper()
print(things)

#7.7 Delete the disease and print the list again
things.remove("SALMONELLA")
print(things)

#9.1 Harry Potter
def good():
    return ["Harry", "Ron", "Hermione"]
good()

#9.2 Get those odds
def get_odds():
    for number in range(1, 10, 2):
        yield number

count = 1
for number in get_odds():
    if count == 3:
        print("The third odd number is", number)
        break
    count += 1