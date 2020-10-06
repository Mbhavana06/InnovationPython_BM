#Question 1:
import math

class Calculate_value:
    def __init__(self,d,h,c):
        self.d = d
        self.h = h
        self.c = c

    def q_Calc(d, h, c):
        print("C- ", type(c), c)
        print("D- ", type(h), h)
        q = math.sqrt(int((2 * c * d) / h))
        return q


d = int(input("Enter the value of D: "))

Q1 = Calculate_value.q_Calc(d, h=30, c=50)
print("The square root is: ",Q1)

#Question 2:
import math
class shape():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(length):
        a = length**2
        return a

    def square(length):
        a = shape.area(length)
        print("The Area of Square is ", a)

shape.square(3)

#Question 3:
class findSum():

    def find_Numbers(input_arr):
        rec = []
        rec_unq = []
        filtered_inp = set(input_arr)
        print(filtered_inp)
        for i in filtered_inp:
            for j in filtered_inp:
                final_item = -(i + j)
                if final_item in filtered_inp:
                    rec.append([i,j,final_item])
                    rec_unq = list(set(map(lambda k: tuple(sorted(k)), rec)))
        print("The combinations which sum-up to 0 are: ", rec_unq)


input_arr = [-25, -10, -7, -3, 2, 4, 8, 10]
findSum.find_Numbers(input_arr)

#Question 4.1:
class A:
    def __init__(self, x=1):
        self.x = x


class der(A):
    def __init__(self, y=2):
        super().__init__()
        self.y = y


def main():
    obj = der()
    print(obj.x, obj.y)


main()
'''
Output: 1 2
'''
#Question 4.2:
class A:
    def __init__(self, x):
        self.x = x

    def count(self, x):
        self.x = self.x + 1


class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y

    def count(self):
        self.y += 1


def main():
    obj = B()
    obj.count()

    print(obj.x, obj.y)


main()
'''
Output: 3 1
'''
#Question 4.3:
class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)

    def multiply(self, i):
        self.i = 4 * i;


class B(A):
    def __init__(self):
        super().__init__()

    def multiply(self, i):
        self.i = 2 * i;


obj = B()
'''
Output: 30
'''
#Question 5:
class Time():
    def __init__(self, hours, minute):
        self.hours = hours
        self.minute = minute

    def add_Time(t1, t2):
        t3 = Time(0, 0)
        if t1.minute + t2.minute > 60:
            t3.hours = (t1.minute + t2.minute) // 60
            t3.hours = t3.hours + t1.hours + t2.hours
            t3.minute = (t1.minute + t2.minute) % 60
        return t3

    def display_Time(self):
        print("The Time is :", self.hours, "hours &", self.minute, "minutes.")

    def display_Minute(self):
        time = (self.hours * 60) + self.minute
        print("The time in minutes is: ", time)

time1=Time(4,45)
time2=Time(2,37)
Total_time = Time.add_Time(time1,time2)
Total_time.display_Time()
Total_time.display_Minute()

# Question 6:
class Person():
    def __init__(self, num):
        self.num = num

        self.yearPasses()
        self.amIOld()

    def yearPasses(self):
        self.num += 1

    def amIOld(self):
        if self.num < 0:
            print("Age is not valid,setting age to 0")
        elif self.num in range(0, 13):
            print("You are young")
        elif self.num in range(13, 20):
            print("You are a teenager")
        else:
            print("You are old")


Age = int(input("Please enter your age: "))

Person(Age)





