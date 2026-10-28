#print ("Hello World");


#Enter the name 
#print ("Abhishek"); print("hi")


'''we are checking code 
it is wrong or not 
to execute multiple lines of codes'''

#print("test"); print("hello py")

#print("This is demo of print", end="****    ")
#print("\n this", "is","demo","of","print",sep="-")

#print("House-" *5)

#print("5" * 6)

#name = "Abhishek"
#profession ="Py developer"
#experience = 5

#print("Hello,i am", name, ".i am a", profession, "professionally.  and i have around", experience,"years experience with it!")

'''x =5
print("x :",x)
print(type(x))
x ="Hello World"
print("x :",x)
print(type(x))
x = 20.5
print("x :",x)
print(type(x))
x = 1j
print("x :",x)
print(type(x))
x = ["apple", "banana", "cherry"]
print("x :",x)
print(type(x))
x = ("apple","banan","cherry")
print("x :",x)
print(type(x))
x = range(6)
print("x :",x)
print(type(x))
x = {"name" : "Abhi" , "age" : 30}
print("x :",x)
print(type(x))
x = {"apple", "banana", "cherry"}
print("x :",x)
print(type(x))
x = frozenset({"apple","banana","cherry"})
print("x :",x)
print(type(x))
x = True
print("x :",x)
print(type(x))
x = b"Hello"
print("x :",x)
print(type(x))
x = bytearray(5)
print("x :",x)
print(type(x))
x = memoryview(bytes(5))
print("x :",x)
print(type(x))
x = None
print("x :",x)
print(type(x))'''

#operator
'''x = 10
y = 15
z = x + y

print(x+y)
print(z)

z = x-y
print(z)
print(x-y)

z = y-x
print(z)
print(y-z)


z = x* y
print(z)
print(x*y)

z= x/y
print(z)
print(x/y)

z=y/x
print(z)
print(y/x)'''

'''x=10
y=14

print(x//y)

print(5%3)  #modules

print(2**3)'''

'''a= 10
b=15
print("a==b", a==b)
print("a<b", a<b)
print("a>b",a>b)
print("a<=b", a<=b)
print("a.=",a>=b)


a=10
b=12
c=14

print(a<b and b>a)
print(a<b or b<c)

print(a is 10)
print(a is 12)

print(a is not 10)
print(a is not 12)'''


#input function
#input function alway retunrs a string

'''name = input("please enter your name :")
print("hello", name)


x = input("enter first value")
y = input("enter second value")

z = int(x) + int(y)

print("sum", z)


x= input("first value:")
y = input("second value")

z = int(x) *  int(y) #multification

print(z) #print the output'''

'''print("2==2 :",2==2)
print("2==2. :",2==2.)

print("2==2.5:",2==2.5)

print('abc'== 'abc')

abc =2
print("abc" == abc)'''

#if else
'''age = 19

if age >= 18:
    print("eligible")

age = input("Enter age to check")
if age >=21:
    print("Eligible for marrige")'''

#Check the number is possitive or negative
'''number = int(input("Enter the number"))
if number  >=0:
    print("Number is possitive")
else :
    print("number is negative")'''

#check the number is even or add
'''number = int(input("Enter number: "))
if number%2==0:
    print("It is even")
else :
    print("it is odd")'''

'''marks = int(input("Enter the marks"))
if marks >= 40:
    print("Passed")
else :
    print("Failed")'''

'''number = int(input("enter the number:"))
if number >=0:
    print("possitive")
elif number <0:
    print("Negative")
else:
    print("Zero")'''

'''x = 20
y = 30

if x>y:
    print("x is larger")
else:
    print("y is larger")'''

#check number is divisible by 3 and 5

'''number = 30

if number/3==0:
    print("it is divisible by 3")
elif number/5==0:
    print("it is divisible by 5")
else:
    print("it is not divible by 3 and 5")'''

#check score with grade 
'''score = 54
if score>=90:
    print("Grade A")
elif score>75:
    print("Grade B")
elif score>50:
    print("Grade c")
else:
    print("Grade F")'''


#loop
'''num =1
while num <=10:
    print(num *5)
    num+=1'''

#write a number more than 5 from 1 to 10
'''num =1
while num  <=10:
    if num >5:
        print(num)
        num +=1'''

'''num =1
while num <=20:
    if num%3==0 :
        print(num)
    num +=1'''

'''num = 5
sum = 1
while num>=1:
    sum *=num
    num-= 1
print(sum)'''

'''Dry run  = running code without executing it 
num(>=1)        sum 
5                1
4                5
3                20
2                60
1                120
0                120

output = 120 
'''

#Write a Python program that:
'''1. Asks the user for their name.
2. Asks the user for their age.
3. Prints a message: "Hello <name>, you are <age> years old."
Use input() and print().'''
'''name = input("Enter your name :")
age  = int(input("Enter your age :"))

print("Hello", name, "youu are",age,"years old")'''


#Write a Python program that:
'''1. Takes two numbers a = 12, b = 5.
2. Prints: a + b, a - b, a * b, a / b, a % b, a ** b.
3. Also prints whether a is greater than b.'''
'''a=12
b=5
print("a+b :",a+b)
print("a-b :",a-b)
print("a*b :",a*b)
print("a/b :",a/b)
print("a%b :",a%b)
print("a**b :",a**b)

if a>b:
    print("a is greater than b")
else:
    print("a is less than b")'''

#Create a complete command-line expense tracker for three expenses. Use variables, 
# literals, input, arithmetic expressions, comments, correct indentation, and 
# suitable data types. Display the total and whether the total exceeds a user-defined budget.

#Take budget from the the user
'''budget = float(input("Enter your budget :")) #user defined budget

#Take three expenses from the user
xpense1 = float(input("Enter the first expense :"))
expense2 = float(input("Enter the second expense :"))
expense3 = float(input("Enter the third expense :"))

#Calculate total expense 
total = expense1+expense2+expense3

#Display the total
print("Total expense :", total) 

#whether the total exceeds a user-defined budget.
if total<=budget:
    print("within budget")
else:
    print("budget exceeded!")'''

#Create a program that accepts two values and demonstrates equality, inequality, greater-than, 
# less-than, identity, and membership operations using appropriate Python objects.
'''a= int(input("Enter first value"))
b= int()

   '''


#While loop
#write program usning while loop to print 1 to 5
'''num = 1
while num<=5:
    print(num)
    num+=1'''

#write program for print even number from 2 to 10
'''num =2 
while num <= 10:
    if num % 2 == 0:
        print(num)
    num+=1'''

#write a program to print odd number from 1 to 9 using while loop
'''num = 1
while num <= 9:
    if num % 2 ==1:
        print(num)
    num+=1'''

#write code to print number from 10 down to 1
'''num = 10
while num >= 1:
    print(num)
    num -= 1'''

#write code to calculate sum of number from 1 to 10
'''num =1
sum = 0
while num <= 10:
    sum+=num
    num+=1
    print(sum)'''

#write code to multifiaction of 5 from 1 to 40
'''num = 1
while num <= 10:
    print(num * 5)
    num +=1'''


    #reberse the number 76543
'''num = 76543
result =0
while num > 0:
    temp = num % 10
    result = result * 10
    result = result + temp
    num  = num // 10
print(result)'''

#for loop

'''for count in range(100):
    print(count)'''

'''for num in range(0,5):
    print(num)'''

'''for num in range(2,6):
    print(num)'''

#write a code from 1 to 5
'''for num in range(1,6):
    print(num)'''

#even number 1 to 10
'''for count in range(1,11):
    if count % 2==0:
        print(count)'''

#odd 
'''for count in range(1,10):
    if count % 2==1:
        print(count)'''

# down num10 to 1
'''for count in range(10,0,-1):
    print(count)'''

#sum 1 to 10
'''sum = 0
for count in range(1,10):
    sum += count
print(sum)'''

#multification 5 
'''for count in range(1,11):
    print(count * 5)'''

'''for count in range(1,11):
    print(f'5 x {count} = {5 * count}')'''

# 1 to 20 divisible 3
'''for count in range(1,20):
    if count % 3==0:
        print(count)'''

#factorial 5 
num =5
fac =1
'''for count in range(1,num):
    fac = fac * count
print(fac)'''

#break and continue
'''num = 1
while num <= 10:
    if num == 5:
        break
    else:
        print(num)
    num += 1'''

'''num = 1
while num <= 10:
    num += 1
    if num == 5:
        continue
    else:
        print(num)'''

#1 to 10 divisible by 7
'''num =1
while num <= 10:
    num +=1
    if num % 7 == 0:
        break
    else:
        print(num)'''

#1 to 10 skip even number 
'''num =1
while num <= 10:
    num += 1
    if num % 2 == 0:
        continue
    else:
        print(num)'''


#List 
'''numbers = []
numbers = [10,20,30,40,50]
print(numbers)

print(type(numbers))

print(f'first element :  {numbers[0]}')
print(f'second  element :  {numbers[1]}')
print(f'third element :  {numbers[2]}')
print(f'fourth element :  {numbers[3]}')
print(f'five element :  {numbers[4]}')

numbers[1]= 100
print(f'second element : {numbers[1]}')
print(numbers)

numbers[0] = numbers[2]
print(numbers)

print(len(numbers))'''

'''myList = ["one",2,2.5,True,False,[1,2,3]]
print(len(myList))
print(myList)
myList[0] =1
print(myList)
print(type(myList))

del myList[0]
print(len(myList))
print(myList)


print(myList[0])
print(myList[3])'''

'''del myList
print(myList)
print(myList[0])'''

'''print(myList[-1])
print(myList[-3])'''

'''list = [1,2,3,4,5]
print(list)
print(f'length  of list : {len(list)}')

list.append(6)
print(list)
print(len(list))

list.insert(0,0)
print(list)
print(f'length of list : {len(list)}')'''


#loop with list
'''list = [5,4,3,2,1]

for index in range(len(list)):
    print("Element :", list[index])

for index in range(len(list)):
    print(f'list[{index}] ->', list[index])'''

'''my_list = []

for conut in    range(1,11):
    my_list.append(conut)
print(my_list)


for index in range(len(my_list)):
    my_list[index] = my_list[index] + 10
print(my_list)'''

#swap the variables
a= 10
b= 20

#1 
'''b = a+b
a = b-a
b = b-a
print(a)
print(b)'''

#2
'''c = b
b= a
a = c
print(a)
print(b)'''

#3
'''b = a * b
a = b // a
b = b // a
print(a)
print(b)'''

'''a,b = b,a
print(a)
print(b)'''

#list sort (bobble sort)
'''list = [8,10,6,2,4]
for index1 in range(len(list)-1):
    for index in range(len(list)-1):
        if list[index] > list[index+1]:
            list[index], list[index+1] = list[index+1] , list[index]

print(list)'''

'''count = 0
list = [8,10,6,2,4]
for index1 in range(len(list)- 1):
    for index in range(len(list)- (index1+1)):
        count +=1
        if list[index] > list[index+1]:
            list[index], list[index+1] = list[index+1] , list[index]

print(list)
print("loop ran :", count,"times")'''

#list = [8,10,6,2,4]
'''list  = [2,4,6,8,10]

count=0
swapped = True
for index1 in range(len(list)- 1):
    swapped = False
    for index in range(len(list)- (index1+1)):
        count +=1
        if list[index] > list[index+1]:
            list[index], list[index+1] = list[index+1] , list[index]
        if swapped == False:
            break  

print(list)
print("loop ran :", count,"times")'''

#using while loop 

'''list = [2,4,6,8,10]

swapped = True
count = 0
while swapped:
    swapped  = False
    for index in range(len(list)-1):
        count +=1
        if list[index] > list[index +1]:
            swapped = True
            list[index], list[index +1] = list[index +1], list[index]
print(list)
print(count)'''

#practice for loop 
#Write a program to print even numbers from 2 to 10 using a for loop.
'''for count in range(2,11,2):
    print(count)'''
'''for count in range(2,11):
    if count % 2 == 0:
        print(count)'''

#print odd number from 1 to 9
'''for count in range(1,10,2):
    print(count)'''
'''for count in range(1,10):
    if count % 2 != 0:
        print(count)'''

#print the number from 10 down to 1
'''for count in range(10,1,-1):
    print(count)'''

#print sum of number from 1 to 10
'''total = 0
for count in range(1,11):
    total = total + count
    
print("Total : ",total)'''

#print the number of multiplification of 5 
'''num = 5
for count in range(1,11):
    print(count * 5)'''

#Write a program to print each item from the list ["Apple", "Banana", "Mango"].

'''list = ["Apple", "Banana", "Mango"]
for list in list:
    print(list)'''

'''list = ["Apple","Banana","Mango","Orange"]
for list in list:
    #print(list)
    print(len(list))'''

'''list = ["Apple","Banana","Mango","Orange"]
for list in list:
    print(len(list))'''

#Write a program to print each character of the string "Python" using a for loop.
'''text = "python"
for char in text:
    print(char)'''

#print the number from 1 to 20 which are  divisible by 3 
'''for count in range(1,21):
    if count % 3 ==0:
        print(count)'''

#write a prograame to find factorial of 5 using for loop
'''fac = 1
for count in range(1,6):
    fac = fac * count
    print(fac)'''

#write programme to ptint only possitive numbers [-3, 5, -1, 8, 0, 4].
'''list = [-3, 5, -1, 8, 0, 4]
for index in list:
    if index > 0:
        print(index)'''

#Write a program to print numbers from 1 to 10 but skip multiples of 3 using continue.
'''for index in range(1,11):
    if index % 3 == 0:
        continue
    print(index)'''

#Write a program to calculate the average of [70, 80, 90, 60, 100] using a for loop.
'''list = [70,80,60,90,100]
total =0
for index in range(len(list)):
    #print(index)
    total = total + list[index]
average = total / len(list)
print(average)'''

#Write a program to print numbers from 1 to 10 and stop the loop when the number reaches 6 using break.
'''for index in range(1,11):
    if index == 6:
        break
    print(index)'''

#Write a program to print numbers from 1 to 10 but skip number 5 using continue.
'''for index in range(1,11):
    if index == 5:
        continue
    print(index)'''

#Write a program to print numbers from 1 to 10, skipping all even numbers.
'''for index in range(1,11):'''

#write aprogramme to print num from 10 down 1 only odd nunber 
'''for index in range(10,0,-1):
    if index % 2 !=0:
        print(index)'''


#list operations 
'''list_1 =[1]
list_2 =list_1
list_1[0]=2

print(list_2)'''


#slice opration
'''my_list = [10,8,6,4,2]
new_list = my_list[1:4]
print(new_list)

new_list = my_list[0:]
print(new_list)

list = []
for index in range(0,500):
    list.append(index+1)

    #175-450
myNewList = list[174 : 450]
print(myNewList)'''

'''my_list = [10,8,6,2,4]
print("21 in my list", 21 in my_list)

my_list1 = my_list[:]

my_list1[2] = 18
print("18 in list", 18 in my_list1)
print("20 in list", 20 in my_list1)'''


'''row = []
for i in range(8):
    row.append("white_pawn")
print(row)
print(len(row))'''


#list comprehnsion
'''row = ["white_pawn1" for i in range(8)]
print(row)
print(len(row))'''

'''squares = [x ** 2 for x in range(10)]
print(squares)

squares = [x ** 2 for x in range(1,11)]
print(squares)'''

'''twos = [2 ** i for i in range(8)]
print(twos)'''

'''evenNumber = [x for x in range(1,11) if x % 2 == 0]
print(evenNumber)'''

'''squares = [ x** 2 for x in range(0,9)]
print(squares)'''


#print the odd number from the list 
'''numbers  = [1, 2, 4, 9,8, 16, 32,33, 64, 128]
oddNumber = [x for x in numbers if x % 2 != 0]
print(oddNumber)'''






#Two dimension array 
'''board= []
for i in range(8):
    row = ["Empty" for i in range(8)]
    board.append(row)

#print(board)

board[0][0]  = "Rooks"
board[0][7]  = "Rooks"
board[7][0]  = "Rooks"
board[7][7]  = "Rooks"

print(board)

board[0][1] = "knight"
board[0][6]  = "Rooks"
board[7][1]  = "Rooks"
board[7][6]  = "Rooks"'''

#temps = [[0.0 for h in range(24)] for d in range(31)]
#print(temps)

'''temps = [[h for h in range(24)] for d in range(31)]
#print(temps)
sum = 0
for i in range(len(temps)):
    sum += temps[i][11]
average = sum / len(temps)
print(average)

greater = -9999999999
for row in range(len(temps)):
    for col in range(24):
        if greater < temps[row][col]:
            greater = temps[row][col]
print("greater :", greater)'''


#Function  -------------------

'''def message():
    print("Enter the value :")'''


#print("Starting now")
#message()
#print("Completed now")

#print("Enter the value")
#message()
#a = int(input())

#print("Enter the value")
#message()
#b = int(input())

#print("Enter the value")
#message()
#c = int(input())


'''def greet(name):  #parameterised function
    print("Hello", name)

name  = input("Enter your name :")
greet(name)         #Argumented function invocation'''


'''def greetWithdetails(firstName, roll):
    print("Hello RollNumber", roll, " ",firstName)

name = input("Enter your name :")
roll = int(input("Enter your roll number :"))
greetWithdetails(name,roll)
greetWithdetails(roll,name)'''

'''def message(what, number):
    print("Enter", what, "number",number)


message("telephone",11)
message("price",5)
message("number",number)'''


'''def message(what, number):
    print("Enter", what, "number",number)

#def message(number,what,xyz):
    #print("enter",what,"number",number)

message("telephone", 11)
message("price",5)
message("number", "number")

message(number=11,what="telephone")
#message(number=11,what="telephone",xyz="xyz")'''

'''def adding(a,b,c):
    print(a,"+", b,"+",c,"=",a+b+c)

adding(1,2,3)
adding(c=1,b=2,a=3)
adding(3,c=1,b=2)
#adding(a=3,1,c=2)'''


'''def happy_new_year():
    print("Three")
    print("Two")
    print("One")
    return
    print("Four")

happy_new_year()

def greet(wishes = True ):
    print(1)
    print(2)
    print(3)
    if not wishes:
        return
    print("Happy new years")

greet(False)'''

'''def sum(a,b):
    return a+b

result = sum(11,32)
print(result)'''

'''def sum(a,b,c,d,e):
    return [a+5,b+5,c+5,d+10,e]

result = sum(11,32,55,90,1)
print(result[0])
print(result[1])
print(result[2])

print(result[3])

print(result[4])'''

'''value = None
if value is None:
    print("Sorry, you don't carry any number")
print(type(None))
print(type(value))


def hello(check):
    if check is True:
        return

result = hello(False)
print(result)

result = hello(True)
print(result)

def strange_function(n):
    if (n % 2 ==0):
        return True

print(strange_function(2))
print(strange_function(1))
'''

'''def strange_list_fun(n):
    strange_list = []
    for i in range(0,n):
        strange_list.insert(0,i)
    return strange_list
print(strange_list_fun(5))'''

'''def greet():
    print("Hello,Python!")

greet()'''

'''def welcome(name):
    print("welcome you",name)

welcome("Abhishek")

def multiple(a,b):
    return a*b

result= multiple(4,5)
print(result)

def square(number):
    return number * number

out = square(2)
print(out)


def even(number):
    if number % 2 ==0:
        return "Even"

check = even(32)
print(check)'''

#scope
'''def scope_test():
    x = 123
scope_test()

def my_function():
    print("Do I know that variable?", var)
var = 1
my_function()
print(var)


var =2
def mult_by_var(x):
    return x * var
print(mult_by_var(7))

var = 7
def mult(x):
    var = 5
    return x * var
print(mult(7))'''

'''def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)'''

'''var = 2
print(var)

def return_var():
    global var 
    var = 5
    return var
print(return_var())
print(var)'''

'''def my_funtion(n):
    print("I got",n)
    n +=1
    print("I have", n)
var = 1
my_funtion(var)
print(var)'''


'''def my_function(my_list_1):
    print("print #1",my_list_1)
    print("print #2", my_list_2)
    my_list_1 = [0,1]
    print("print #3", my_list_1)
    print("print #4", my_list_2)

my_list_2 = [2,3]
my_funtion(my_list_2)
print("print #5", my_list_2)'''

'''def my_function(my_list_1):
    print("print #1", my_list_1)
    print("print #2", my_list_2)
    #my_list_1 = [0,1]  #new list created locally
    my_list_1.append(5)
    print("print #3", my_list_1)
    print("print #4", my_list_2)
    del my_list_1[0]
    print("print #5", my_list_1)
    print("print #6", my_list_2)

my_list_2 = [2,3]
my_function(my_list_2)
print("print #7", my_list_2)'''

'''tuple_1 = (1,2,3,4,8)
print("tuple_1", tuple_1)
print("Type of tuple_1", type(tuple_1))

tuple_2 = 1.,.5,.25,.125
print("tuple_2:",tuple_2)
print("type of tuple_2", type(tuple_2))
tuple_3 = 1,2,3,4,5
print("tuple_3",tuple_3)
print("Type of tuple_3",type(tuple_3))'''

#tuple operations
my_tuple = (1,10,100,1000)
#my_tuple.append(10000)
#del my_tuple[0]
#my_tuple[1] = -10
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])













