#block of statement that perform a specific task
#def fun_name(Param 1, param 2):Function Defination
#some work
#return
#calculate the input number 
#function drfination
# def calc_sum(a,b):
#     c=a+b
#     return c;
# a= int(input('enter your value '))
# b= int(input('enter your value '))
#print(calc_sum(a,b));#function call(arguments)
# average of 3 number
# def avrg_value(e,f,g):
#     sum =e+f+g
#     avg =sum/3
#     return avg;
# e= int(input('enter your value '))
# f= int(input('enter your value '))
# g= int(input('enter your value '))
# print(avrg_value(e,f,g))
##################### function type###########
#built in function (print(),len(),type(),range())
#user defined function(user can create this in code)
# WAF to print the length of a list.(kist is the parameter)
# city=["delhi","HP","noida","mumbai","chennai"]
# def print_len(city):
#     print(len(city))
# print_len(city)
# city=["delhi","HP","noida","mumbai","chennai"]
# Heros=["thor","ironman","Spider","wolvarean"]
# def print_len(list):
#     print(len(list))
# #so this code can be print the len fo all the list which we have output just we want to call them
# print_len(city)
# print_len(Heros)
# #WAF to print the elemts of a list in a single line .(list os the patameter)
# def print_list(list):
#     for item in list:
#         print(item,end=" ")
# print_list(Heros)
# #WAF to find the factorial of n (n is the parameter)
# n = int(input("enter the number for factorial "))
# def fac(n):
#     torial=1
#     for i in range(1,n+1):
#         torial *= i
#     print(torial)
# print(fac(n));
#WAF to covert USD to INR
# USD=int(input("enter the number of USD which you want to convert"))

# def convt (USD):
#     inr = USD*83
#     print(USD,"USD=",inr,"INR")
# convt(USD)
# WAF check number is odd or even
# n = int(input("enter your number to check its odd or ever"))
# def check (n):
#     if(n%2==0):
#         print("it is even number")
#     else:
#         print("it is not even")
# check(n)
################Recursion#####################
# when a  function call itself repeatedly
def show(n):
    if(n==0):
        return# this is base case with out this base case iyr recursion will e continue for life 
    print(n)
    show(n-1); # so now it can run up to the value when the n==0;
show(4)

