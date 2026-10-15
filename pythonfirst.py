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

#list sort

