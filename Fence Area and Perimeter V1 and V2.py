# Fence Area and Perimeter Calculator
# Author: Harper Lewis
# Date: 2024-09-27
# Version 1

'''go_again = ""
while go_again == "":
  width = float(input("Width in M: "))
  length = float(input("Length in M: "))
  perimeter = 2 * width + 2 * length
  area = width * length
  if width <= 0 or length <= 0:
      print("I dont understand, please enter a number above 0")
      
  else:    
    perimeter = 2 * width + 2* length
    area = width * length 
  
    print(f"the perimeter of the fence is {perimeter}M, and the area is {area}M . ")
  

  go_again = input("press enter to continue or any other key to quit")'''

# V2, using while True and Try and Except 
start = True
while start:
    print("Hello, welcome to fence perimeter and area calculator")# Introduce the code
    print("-----------------------------------------------------")
    print("please enter positive numbers for width and height")
  
    while True:
      try: 
          width = float(input("Please enter width in Units: ")) # Ask user for width
          if width <= 0 : # Check if width is greater than 0
            width = float(input("Please enter a new width greater than 0")) # If width is lower than 0, ask for a new number 
          height = float(input("Please enter Height in Units:  ")) # Ask User for Height 
          if height <= 0 : # Check the height is 
            height = float(input("Please enter a new Height greater than 0")) # If Height is lower than 0, ask for a new number greater than 0
                         
          
        
          perimeter = 2* width + 2* height # Calculate perimeter in relation to width and length
          area = width * height # calculate area in relation to width and length
 
          print(f"The perimeter of the fence is {perimeter} units, and the area is {area}units ^2") # State perimeter and area
          break
               
      except ValueError:
          print("Error, Please enter a Number, rather than a variable") # If the user enters a letter or symbol, I ask for a valid number.
    again = input("do you want to continue the code, press enter to continue or any other key to quit")  # Ask the user if they wants to continue or not
    if again != "": # If user enters any thing but enter, Quit the code, if they enter enter, the code restarts. 
        print("Thanks for using my fence calculator")
        start = False
                
      

    
    
      
    
    







    