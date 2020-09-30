# Question 1
a=10
List = ["Hello",45,a,7.0,(3+a),"Consultadd", 25, 99.9, "Python",60]
print(List)

# question 2: Create a list of size 5 and execute the slicing structure:

list=[2,4,6,8,10]
print(list[1:5])
print(list[::-1])
# Write a program to get the sum and multiply of all the items in a given list:

L=[10,20,30,40,50,60]

print(sum(L))

product = 1

for e in L:
    product = product*e

print(product)

#Question 4:

Num_List = []
Length = int(input("Enter the length of the list:"))

for e in range(1,Length+1):
    element = int(input("Enter Value:"))
    Num_List.append(element)
print("Max value =",max(Num_List))
print("Min value =",min(Num_List))

#Question 5
list1 = [1,2,3,4,5,6,7,8,9,10]
new_list =[]

for e in list1:
    if e%2!=0:
        new_list.append(e)
print(new_list)

# Question 6:
list2=[]
count = 0
for e in range(1,31):
    count+=1
    if count < 5 or count > 24:
        list2.append(e * e)
print(list2)

# Question 7:
list3 = [[1,3,57,9,10],[2,4,6,8]]
list_new = []

for e in list3[0][0:-1]:
   list_new.append(e)

for e in list3[1]:
       list_new.append(e)

print(list_new)

# Question 8:
a={'1':10,'2':20}
b={'3':30,'4':40}

a.update(b)
print(a)

#Question 9:
num = int(input("enter a number:"))
d = dict()

for x in  range(1,num+1):
    d[x]=x*x

print(d)

# Question 10:
list_1 = []
Tuple_1 = ()

len = int(input("enter max range"))

for e in range(1,len):
    value = int(input("enter value"))
    list_1.append(e)

Tuple_1 = tuple(list_1)
print(list_1)
print(Tuple_1)

# Question 11 & 12 are repeated same as 1& 2:

# Questio 13:
X = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

print( X[5][0:4])

print( X[6:8])

new_List = []
for e in range(0,len(X)):
    if e%2 ==0:
        new_List.append(X[e])
print(new_List)

print(X[::-1])

print(X[5][5][0])

X.clear()
print(X)

# Question 14:
listR=[]
listXR = []
i = 0

for i in range(1000):
     listR.append(i)
     i+=1
print(listR)

# Question 16:
for e in range(1,100):
    if e%3==0 and 2%2==0:
        print(e)

#Question 17:
String="helloiambhavanana"

reverse_string = String[::-1]

print(reverse_string)
count=0


for e in reverse_string:
    count+=1
    if (e == 'A' or e == 'a' or e == 'E' or e == 'e' or e == 'I'
            or e == 'i' or e == 'O' or e == 'o' or e == 'U' or e == 'u'):
        print("index no:",count,"vowel:",e)
#Question 18:
string1="Hello my name is Bhavana"

string1=string1.split(' ')

for e in string1:
    if len(e)%2 ==0:
        print(e)

#Question 19:
x=[1,2,3,4,5,6,7,8,9,-1]
target = 8
y=[]
for i in range(len(x)):
    first_p = x[i]
    second_p = target - first_p
    if second_p in x:
        y.append([first_p,second_p])
    else:
        continue
print(y)
#Question 20:
odd_list=[]
even_list=[]
boo=True


while len(odd_list)<6 or len(even_list)<6:
    num = int(input("enter a number in the range of 150"))
    if num >150:
        print("Limit exceeded, enter a number lower than 150")
        boo=False
        break
    if num%2==0:
            even_list.append(num)
    else:
            odd_list.append(num)


if boo == True:
    print(even_list)
    print(odd_list)
print("Sum of Odd List is:", sum(odd_list))
print("Sum of Even List is:", sum(even_list))
print("Max of odd list is:", max(odd_list))
print("Max of even list is:", max(even_list))

#Question 21:
x="bhavanaMeena1234"
for e in x:
    if e.isalpha() == True:
        counter=x.count(e)
        print(e,"=",counter)
#Question 22:
tuple_1 = (1,2,3,4,5,6,7,8,9,10)
l1=[]

for e in tuple_1:
    if e%2==0:
        l1.append(e)
l1=tuple(l1)









