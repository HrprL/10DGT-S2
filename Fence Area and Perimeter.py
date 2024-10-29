# Conditional statements and while loops
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
    print("Hello, welcome to fence perimeter and area calculator")
    print("-----------------------------------------------------")
    print("please enter positive numbers for width and height")
  
    while True:
      try: 
          width = float(input("Please enter width in Units: ")) 
          length = float(input("Please enter Height in Units:  "))
          if width <= 0 : 
            width = float(input("Please enter a new width greater than 0"))
          if length <= 0 :
            length = float(input("Please enter a new Height greater than 0"))
                         
          
        
          perimeter = 2* width + 2* length
          area = width * length 

          print(f"The perimeter of the fence is {perimeter} units, and the area is {area}units ^2")
          break
               
      except ValueError:
          print("Error, Please enter a Valid Number")
    again = input("do you want to continue the code, press enter to quit")
    if again != "":
        start = False
                
      

    
    
      
    
    







    