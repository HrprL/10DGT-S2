# Conditional statements and while loops
# Author: Juergen Lier
# Date: 2024-09-27
# Version 1
# TODO: Create a program that asks a user a question
#  and returns a response based on the answer of the user


# Main loop. Keeps running until a condition is met
keep_going = ""
while keep_going == "":
    # asks the user if they like coffee
    like_coffee = input("Do you like coffee ").lower() # converts users answer lowercase through .lower 

    if  like_coffee == "yes"  or like_coffee == "y":
        print("I like coffee too")
    elif like_coffee == "no" or like_coffee == "n": 
        print("you are missing out")
            
        like_tea = input("Would you like tea instead? ").upper()
        if like_tea == "NO" or like_tea == "N":
            print("Sorry that is all I have")
        elif like_tea == "YES" or like_tea == "Y":
            print("good for you")
        
    else: 
        print(" I don't understand, answer yes or no")
    
    keep_going = input("press  <enter> to continue or any other key to quit")