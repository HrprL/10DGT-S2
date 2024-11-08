# Date 24/11/08
#Author: Harper Lewis
# Fence Cost Calculator Utilising Functions 




def valid_num(go):  # Function to use in front of questions, asks for numbers > 0.
      while True:
        try:
            num = float(input(go))
            if  num > 0:  # If the number is higher than 0, return the number 
                return num
            else:
                print("please enter a positive number") # If not, ask for a larger number 
                
        except ValueError: # Ask user to enter a number, rather than a symbol. 
            print("Please enter a valid number")



print ("Hello, welcome to fence perimeter and area calculator")# Introduce the code
print ("-----------------------------------------------------")
print ("please enter positive numbers for all questions asked") # Explain to user the kind of answers the code wants
Start = input("Press enter to use my program or any other button to quit") # Ask the user whether or not they want to utilise the code
while Start == "":
   
        
          m = input("In what unit would you like to measure:")
          width = valid_num(f"Please enter width in {m}:\n ")# Ask user for width in units of their choice
          length = valid_num(f"Please enter Length in {m}:\n ") # Ask User for Height in units of their choice
          cost =  valid_num(f"Please enter the cost per {m} of fence length: \n$") # Ask user for cost in units of their choice
          budget = valid_num(f"Please enter your budget for the fence: \n $") # Ask user for valid budget 
                         
          perimeter = round(2 * width + 2 * length , 2) # Calculate perimeter in relation to width and length
          area = round(width * length , 2) # calculate area in relation to width and length
          total_cost = round(cost * perimeter , 2)  #Calculates the Total Cost of the fence
          affordable_quality = round(budget / perimeter, 2) # Calculates the largest affordable quality for the budget given
          affordable_perimeter = round(perimeter / total_cost * budget, 2) # Calculates the largest affordable perimeter for the budget given
 
          print(f"The perimeter of the fence is {perimeter} {m}, and the area is {area} {m}²\n" "---------------------------------------------------------------------------------\n") 
          print(f"The total cost is {total_cost}")
          if budget > total_cost:    #This set of If loops return to the user whether or not they can afford their budget, and promotes other alternatives
            print(f"Congratulations! You are able to afford the fence with your budget given, alternatively, you can allow yourself a fence of a quality of {affordable_quality} per {m}\n you can also afford a larger fence with a perimeter of {affordable_perimeter} {m}")  
          elif budget == total_cost:
            print("You have the perfect amount of money for this project!")
          elif budget < total_cost: 
            print(f"You are unable to afford this fence, to afford this fence, you could buy a fence with the quality of {affordable_quality} per {m}\n or a smaller fence with a perimeter of {affordable_perimeter} {m}")
           
          
          Start = input("do you want to continue the code, press <enter> to continue or any other key to quit\n")  # Ask the user if they wants to continue or not         



                
    