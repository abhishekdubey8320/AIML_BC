
#Calculator App :

def options():
    print("Welcome to Calculator app :")
    print("Please choose an options below :")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multification")
    print("4. Devision")
    print("5. Average")
    print("6. Exit")

#Addition
def addition_number():
        total = 0
        while True:
             num = int(input("Enter number (-1 to stop :) : "))

             if num == -1: #try 
                  break
             
             total +=num 
        print("==========================")
        print(f"Sum of all numbers : {total}")
        print("==========================")
#Subtract 
def subtract_number():
        first_number = int(input("Enter first number for Subtract :")) #while loop infinite 
        second_number = int(input("Enter second number for Subtract:"))
        sub_number = first_number - second_number
        print("==========================")
        print(f"Subtract : {sub_number}")
        print("==========================")

#Multification
def multification_number():
       multiply = 1 #try
       while True:
            num = int(input("Enter number (-1 to stop) : "))
            if num == -1:
                 break
            multiply *= num
       print("==========================")
       print(f"Multiply of all numbers : {multiply}")
       print("==========================")

#Division
def division_number():
       first_number = int(input("Enter first number for division :")) # while
       second_number = int(input("Enter second number for devision:"))
       div_number = first_number / second_number
       print("==========================")
       print(f"Division : {div_number}")
       print("==========================")


#Average 
def check_average():
       count = 0
       total = 0
       while True:  #try #float
             num = int(input("Enter number (-1 to stop) : "))
             if num == -1:
                  break
             total += num
             count += 1
       average = total / count
       print("==========================")
       print(f"Average of all numbers : {average}")
       print("==========================")

#Select options
while True:
    options()
    try:
        choice = int(input("Enter your choice :"))

        if choice == 1:
            addition_number()
        elif choice == 2:
            subtract_number()
        elif choice == 3:
            multification_number()
        elif choice == 4:
            division_number()
        elif choice == 5:
            check_average()
        elif choice == 6:
            break
        else : 
            print("==========================")
            print("You have entered invalid option!")
            print("==========================")
    except ValueError:
        print("==========================")
        print("Invalid input! Please enter numbers only between 1 to 6.")
        print("==========================")
          


    
       
