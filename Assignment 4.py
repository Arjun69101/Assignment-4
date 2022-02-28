#ASSIGNMENT 4


#___________________Question 1___________________


print('Q1')
print()

# Creating function to solve Tower of Hanoi question
def Tower_of_Hanoi(n , from_rod, to_rod, using_rod):
    if n == 0:
        return
    Tower_of_Hanoi(n-1, from_rod, using_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    Tower_of_Hanoi(n-1, using_rod, to_rod, from_rod)

# Input
n=3
Tower_of_Hanoi(n,'A','C','B')
print()

#___________________Question 2___________________

print('Q2')
print()

# import math 
from math import factorial

# Input
n=5

# Iterative approach
if n==0:
    print(1)
else:

    for i in range(n):

        for j in range(n-i+1):

            # For spaces on the left
            print(end=' ')


        for j in range(i+1):

            # nCr = n!/[(n-r)!*r!]
            print(factorial(i)//(factorial(i-j)*factorial(j)), end=' ')
    
        # Leave a line
        print()

# Recursive approach

def pascals_triangle(n):
    if n==0:
        return 1
    if n == 1:
        return [[1]] 
    else:
        # Recursive call
        result = pascals_triangle(n-1)

        # Calculate current row using info from previous row
        current_row = [1]
        previous_row = result[-1] 

        for i in range(len(previous_row)-1):
            current_row.append(previous_row[i] + previous_row[i+1])
            
        current_row += [1]
        result.append(current_row)
        return result

n=5
triangle = pascals_triangle(n)
for row in triangle:
    print(row)

print()

#___________________Question 3___________________

print('Q3')
print()

First_int=int(input('Enter an integer: '))
Sec_int=int(input('Enter another integer: '))

# Quotient and Remainder
div_result=divmod(First_int,Sec_int)
print('Quotent and remainder : ', div_result)

# Is function callable or not
print('Is function callable : ', callable(divmod))

# Check if a zero is present in tuple
First_int = div_result.count(0)

if First_int in [1,2]:
    print('zero is present in tuple')

else:
    print('zero is not present in tuple')

# Adding (4,5,6) in tuple
result_list=list(div_result)
result_list.append(4)
result_list.append(5)
result_list.append(6)
print('After adding values : ', result_list)

# Filtering out values greater than 4
end_result=[x for x in result_list if x<=4]
end_result=tuple(end_result)
print("Next tuple : ", end_result)

# Converting result to set
end_result=set(end_result)
print('Set : ', end_result)

# Making set immutable
end_result=frozenset(end_result)
print('Immutable set :', end_result)

# Finding max value in set
max_val=max(end_result)
print('Max value of set : ', max_val)

# Hash value of max value
print('Hash value of max value : ', hash(max_val))

print()

#___________________Question 4___________________

print('Q4')
print()

# Creating class called Student
class Student:

    # Constructor
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
        print('Student created')
    
    # Destructor
    def __del__(self):
            print('Destructor called, student deleted')
    
# Values for student 
stud1=Student('Arjun',21104029)

# Deleting student
del stud1

print()

#___________________Question 5___________________

print('Q5')
print()

# Creating class for employees
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print('Employee created.')

    def __del__(self):
        print('Destructor called, employee deleted')


# Input the details of employees
emp1=employee('Mehak',40000)
emp2=employee('Ashok',50000)
emp3=employee('Viren',60000)

# Upodating salary of Mehak
emp1.salary=70000

# Deleting record of Viren.
del emp3

print()

#___________________Question 6___________________

print('Q6')
print()

from itertools import permutations

# Creating set for checking
final_set=set()

# Taking user inputs
George_inp=input('George said: ')
Barbie_inp=input('Barbie said: ')

# Finding variations of word
lower_inp = [x.lower() for x in George_inp]

for y in list(permutations(lower_inp)):
    z=''.join(y)
    final_set.add(z)

# Test for friendship
if Barbie_inp.lower() in final_set :
    print('Their friendship is real')
else:
    print('Their friendship is fake')


#_____________________OVER_____________________












