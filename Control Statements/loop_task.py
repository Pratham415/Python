###  WAP to find power of a given number
# Output :--
# Enter number & Power :2
# 5
# Result of power : 32

# number = int(input("enter the number : "))
# power = int(input("Enter the power : "))
# ans = 1
# for i in range(power):
#     ans = ans * number
# print(ans)

##-----------------------------------------

# > WAP to find factorial of a given number
# Output:--
# Enter the no:5
# The factorial is 120
# num = int(input("Enter the number :"))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(f"Factorial of {num}:", fact)

#----------------------------------------------
# > WAP check the no. Armstrong or not
# Output:--
# Enter one no.: 153
# It is armstrong no

# > WAP to print whether no. is Palindrome or not
# Output :--
# Enter a no.: 1221
# palindrome no
# num = int(input("Enter the number :"))
# if(str(num) == str(num)[::-1]):
#     print("The number is palindrome !")
# else:
#     print("The number is not palindrome")

# > WAP to print Fibonacci Series
# Output:--
# 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

# > WAP to find sum of digit.
# Output:-
# Enter a Number:15
# Sum of digits of a number:6
# num = input("Enter the number : ")
# sum = 0
# for i in range(0,len(num)):
#     sum = int(sum) + int(num[i])
# print(sum) 

# > WAP to find sum of odd digit of entered digit.
# Output:-
# Enter a Number:1567
# Sum of Odd digits of a number:8 ###
num = int(input("Enter the number : "))
sum = 0
for i in range(0,3):
    if i % 2 != 0:
        sum = sum + i 
print(sum)