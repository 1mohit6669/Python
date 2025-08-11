#Write a for loop to print numbers from 1 to 10.
'''for i in range(1,11):
    print(i)'''
#Sum of All Elements in a List
'''number =[10,20,30]
for i in range(len(number)):
    d= sum(number)
print(d)'''
#Count Even and Odd Numbers
'''nums = [12, 15, 9, 10, 32, 7]
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        print("Even")
    else:
        print("Odd")'''
#Print a Multiplication Table
'''table= int(input('enter the table you want to print'))
for i in range(1,11):
    print(f"{table}x{i}={table*i}")'''
#Reverse a String Using Loop
'''stor='mosdfaoaafth'
for i in range(len(stor)-1,-1,-1):
    print(stor[i],end='') ''' # end='' prevents a new line after each character
#Find the Factorial of a Number
'''n= int(input('enter the number for factorial'))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)'''
# Print Only Vowels from a String
'''d= 'though'
vowels = 'aeiou'
for char in d:
    if char.lower() in vowels:
        print(char, end=' ')'''
#Nested Loop to Print a Pattern
'''rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()'''
#Print Prime Numbers in a Range
'''n= int(input('enter the your number'))
m = int(input('enter the second number for range'))
for i in range(n,m):
    if i > 1:  # Prime numbers are greater than 1
        for j in range(2, int(i**0.5) + 1):  # Check divisibility up to the square root of i
            if (i % j) == 0:
                break
        else:
            print(i, end=' ') ''' # If no divisors were found, i is prime
#Fibonacci Sequence (N terms)
'''n= int(input('enter the number'))
a= 0
b= 1
for i in range(n):
    print(a,end=" ")
    c= a + b
    a = b
    b = c'''

# Check for Armstrong Number
'''num =int(input('entert the number'))
sun = 0
t= num
for i in range(len(num)):
    d=num%10
    sum +=d**3
    num //=10
    if sum == t:
        print('number is armstrong')
    else:
        print('its is not')'''
# Check for Palindrome Number
'''d= int(input('enter the number'))
R= 0
for i in range(len(str(d))):
    R = R * 10 + d % 10
    d //= 10
if R == d:
    print('number is not palindrome')
else:
    print('number is  palindrome')'''
# Check for Perfect Number
c= int(input('enter the number to check wether its perfect or not '))
