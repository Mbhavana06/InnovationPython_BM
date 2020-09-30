#Write a program in Python to perform the following operation:
#If a number is divisible by 3 it should print 􏰜Consultadd􏰝 as a string
#If a number is divisible by 5 it should print 􏰜c􏰝 as a string
#If a number is divisible by both 3 and 5 it should print 􏰜Consultadd Python Training􏰝 as a string.

x=3
if x%3==0 & x%5==0:
    print("Consultadd Python Training􏰝")
elif x%3==0:
    print("consultadd")
elif x%5==0:
    print("C")

#Question 2

print("Enter any one option below:")
print('Enter 1 for Addition\nEnter 2 for subtraction\nEnter 3 for Division\nEnetr 4 for Multiplication\nEnetr 5 for Average')

N= int(input("Enter your option"))
First = int(input("Enetr your First number"))
Second = int(input("Enter you Second number"))

if N==1:
    res = First+Second
    if res > 0:
        print("Result:" + str(First+Second))
elif N == 2:
    print("Result:" + str(First - Second))
elif N== 3:
    print("Result:" + str(First/Second))
elif N == 4:
    print("Result:" + str(First*Second))
elif N== 5:
    print("Enter First2 and Second2")
    First2=int(input("Enter First2"))
    Second2=int(input("Enter Second2"))
    print("Result:" + str((First2+Second2)/2))
if res<0:
    print("Negative")

# Question 2
a= 10
b= 20
c= 30
avg=(a+b+c)/3
print(avg)
if avg > a and avg> b and avg> c:
    print(" avg is greater than a,b,c")
elif avg > a and avg > b:
    print(" avg is greater than a & b")
elif avg > a and avg > c:
    print(" avg is greater than a & c")
elif avg > b and avg > c:
    print(" avg is greater than c & b")
elif avg > a:
    print(" avg is greater than a")
elif avg > b:
    print(" avg is greater than b")
elif avg >c:
    print(" avg is greater c")

# Question 4
Num = int(input("Enter a number"))

while Num > 0:
    print("Good Going")
    Num = int(input("Enter a number"))
else:
    print("Its over")

# Question 5:
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        print(i)

# Question:
for i in range(7):
    if (i==3 or i==6):
        continue
    else:
        print (i)
#Question 8:
String1=input("Enter a String:")
Letters=0
Digits=0

for i in String1:
    if i.isdigit()==True:
        Digits+=1
    if i.isalpha()==True:
        Letters+=1
print(Digits)
print(Letters)
# Question 9:
Lucky_Num = 6
boo = True

Num = int(input("Guess the Lucky number:"))

while Num!= Lucky_Num:
    Answer = str(input("Guess Again?").lower())
    if Answer == "no":
        print("Game Over")
        boo = False
        break
    else:
        Num = int(input("Guess the Lucky number:"))
if boo == True:
    print("Correct Guess")

# Question 10:
Lucky_Num = 6
boo = True
Counter = 0

Num = int(input("Guess the Lucky number:"))

while Counter<5:
    Answer = str(input("Guess Again?").lower())
    Counter+=1
    if Answer == "no":
        print("Game Over")
        boo = False
        break
    else:
        Num = int(input("Guess the Lucky number:"))
if Counter ==5:
    print("Max Attempts")


#  Question 7:
Lucky_Num = 6
boo = True
Counter = 0

Num = int(input("Guess the Lucky number:"))

while Num != Lucky_Num and Counter < 5:
    Answer = str(input("Guess Again?").lower())
    Counter += 1
    if Answer == "no":
        print("Game Over")
        boo = False
        break
    else:
        Num = int(input("Guess the Lucky number:"))
if Counter == 5:
    boo = False
    print("Max Attempts")

if boo == True:
    print("Correct Guess")

# Question 8:


















