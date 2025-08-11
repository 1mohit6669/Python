n= int(input("Enter a number: "))
Total = 0
# This code calculates the sum of numbers from 1 to n
for i in range(1, n+1):
    Total += i
print("The sum is:", Total)
# This code calculates the sum of even numbers from 1 to n
Total = 0
for i in range(2, n+1, 2):
    Total += i
print("The sum of even numbers is:", Total)
# This code calculates the sum of odd numbers from 1 to n
Total = 0
for i in range(1, n+1, 2):
    Total += i
print("The sum of odd numbers is:", Total)