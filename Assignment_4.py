#Question1:

def Reverse(string):
    print(string[::-1])

Reverse("bhavana")

#Question 2:
def Upper_Lower(string):
    count_upper=0
    count_lower=0
    for e in string:
        if e.isalpha()== True:
            if e.isupper()==True:
                count_upper+=1
            else:
                count_lower+=1
    print("Number of Lower case characters:",count_lower)
    print("Number of Upper case characters:",count_upper)

string=str(input("Enter a string"))
Upper_Lower(string)

#Question3:
def Unique_list(list):
    uniqueList = []
    for e in list:
        if e not in uniqueList:
            uniqueList.append(e)
    print(uniqueList)

L=[1,2,34,4,5,5,6,7,8,9,6,8]
Unique_list(L)

#Question 4:
def Hyphen_Seperated(words):
    l=words.split('-')
    l.sort()
    print("sorted list:",'-'.join(l))

Hyphen_Seperated("bhavana-meena-dimple-consultadd")

#Question 5:
def Sequence_Upper(limit):
    for i in range(limit):
        line=input("enter line")
        line=line.upper()
        print(line)

limit=int(input("enter number of lines"))

Sequence_Upper(limit)

#Question 6:
def Str_Number(string1,string2):
    a=0
    for e in string1,string2:
        if e.isdigit()== True:
            e=int(e)
            a=e+a
    print(a)

Str_Number("23","56")

#Question7:

def len_Str(str1,str2):
    if len(str1) == len(str2):
        print(str1)
        print(str2)
    elif len(str1)>len(str2):
        print(str1)
    else:
        print(str2)

str1=str(input("Enter string 1:"))
str2=str(input("Enter string 2:"))

len_Str(str1,str2)

#Question 8:
def tuple_Square(n):
    L=[]
    for i in range(21):
        i=i*i
        L.append(i)
    tuple1=tuple(L)
    return tuple1

n=()
print(tuple_Square(n))

#Question 9:
def showNumbers(limit):
    for i in range(limit):
        if i%2==0:
            print(i,"EVEN")
        else:
            print(i,"ODD")

limit=int(input("Please enter the limit"))
showNumbers(limit)

#Question 10:
lis1 = range(21)

is_even = lambda x: x % 2 == 0

lis2 = list(filter(is_even, lis1))

print(lis2)

#Question 11:
li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, li1)))

#Question 12:
try:
    x=5/0
except:
    print("Division by zero error")
#Question 13:
import operator
from functools import reduce

lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
New_List = reduce(operator.add, lists)

print(New_List)

#Question 14:
# Quest (i)
def foo():
    try:
        return 1
    finally:
        return 2
k=foo()
print(k)
# Output:2

#Quest(ii)
# def a():
#     try:
#         f(x,4)
#     finally:
#         print('after f')
#     print('after f?')
#
# a()


#Output:
# NameError: name 'f' is not defined
# after f









