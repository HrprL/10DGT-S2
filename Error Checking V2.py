# Error Checking
# Author: Harper L.
# Date: 2024/10/25
#Version 1

# Code that tests that a valid number isentered(V1) 
'''done = False # Boolean variable set to false
while not done: # while loop that runs until a valid number is entered.
  num = int(input("Please enter your value:"))
  done = True
print(f"The number you entered is {num}")


# Code that tests that a valid number is entered(V2)
# Create a function to call every time I ask the user for
# a number A Chunk of code that does something
# I can use a function over and over. To use a function
# I 'Call it' by writing out its name. 
def test_int_num(question): 
    # The 'Question' Is a placeholder 
  done = False
  while not done:
     try: #This tries for a valid input
        num = int(input(question))
        done = True
     except ValueError: 
        print("That is not a valid number, please enter a whole number and try again")
  
  return(num) # GIves back the value of num 
              # So that I can use it outside the function
#Main Routine



num_1 = test_int_num("Please enter your first number:")    
print(f"You entered {num_1}.")
num_2 = test_int_num("Please enter your second number")
print(f"you entered {num_2}.")   
num_3 = test_int_num("Please enter your third number")
print(f"you entered {num_3}.")   


sum = num_1 + num_2 + num_3
subtract1 = num_1 - num_2 - num_3
subtract2 = num_2 - num_1 - num_3
subtract3 = num_3 - num_2 - num_1
answer = input(f"What operation would you like to run with these numbers, add  or subtract, answer s for subtraction or a for addition")

if answer == "s": 
 order=input(f"What variable do you want to subtract from?,{num_1}, {num_2}, {num_3}, enter 1 for first num_1, 2 for num_2 or 3 for num_3")
 

 if order == "1":
  print(f"The equation is {num_1} - {num_2} - {num_3} = {subtract1}") 

 elif order == "2":
  print(f"The equation is {num_2} - {num_1} - {num_3} = {subtract2}")
 elif order == "3":
  print(f"The equation is {num_3} - {num_2} - {num_1} = {subtract3}") 

 else: 
  print("please enter a valid number, 1 for first number, 2 for second number or 3 for third number?")
  order=input(f"What variable do you want to subtract from?,{num_1}, {num_2}, {num_3}, enter 1 for first num_1, 2 for num_2 or 3 for num_3")





if answer == "a":
 print(f"the total of {num_1}, {num_2} and {num_3} is {sum}.")


# Version 3, Refining my code. Making it more pythonic 
#Ask the user to pick a number in a range .
'''def valid_num(question, low, high):
    error = f"That is not a valid number. Please enter an integer between {low} and {high}"
    while True:
        try:
           response = int(input(question))
           if low <= response <= high: #if response >= low and response <= high:

             break
           else: 
              print(error)
              print()
        except ValueError:
          print(error)
    return response 
# main routine
num_1 = valid_num("enter a number between 1 and 15:", 1, 15)
print(f"you entered {num_1}")
num_2 = valid_num("now enter a number between 50 and 100", 50, 100)
print(f"you entered {num_2}")

num_3 = valid_num("now enter a number between 70 and 80", 70, 80)
print(f"you entered {num_3}")

# return the product of all three answers
multiply = num_1 * num_2 * num_3 
print(f"the product of your numbers is {multiply}")
sum = num_1 + num_2 + num_3
print(f"the total of {num_1}, {num_2} and {num_3} is {sum}.")
