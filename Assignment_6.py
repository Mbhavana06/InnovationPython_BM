#Question 1:
def Div_By_3(num):
    if num%3!=0 and num%7==0:
        print(num, "is not divisible 3 but its a multiple of 7")

def Find_Value(func):
    number=int(input("Enter a number"))
    value=func(number)


Find_Value(Div_By_3)
#Question 2:
def Multiply(n):
    return n*n

l1=[1,2,3,4]

print(list(map(Multiply,l1)))

#Question 3:
string = "Consultadd"
empty_list =list(string)

outcome = [n for n in empty_list if n.isupper() == True]

print(outcome)

#Question 4:
Student = ['Smit', 'Jaya', 'Rayyan']
Capital = ['CSE', 'Networking', 'Operating System']

Dict_Student = dict(zip(Student, Capital))
print(Dict_Student)

#Question 5: Done

#Question 6:
def reverse(string1):
    print(string1[::-1])


def print_rev(func):
    str1 = "Consultadd Training"
    final=func(str1)

print_rev(reverse)

#Question 7:
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide_1(a, b):
    print(a/b)
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

divide_1(a,b)

#Question 8:
'''
1) React for a Responsive Web Front-End Development: Airbnb, Dropbox, BBC, Facebook, New York Times, and Reddit.
2) Angular Front-End Development: Netflix, Upwork, IBM, Goodfilms.
3) Vue.js Web App Front-End Development: 9gag, Nintendo, GitLab, Behance, and Laravel
4) Flutter: Google ads, Alibaba, Birch Finance, Cryptograph, and Hookle.
5)Foundation for Mobile-First Front-End Development: Hp, Adobe, Amazon, EA, National Geographic, Pixar, Mozilla, Ford

'''
