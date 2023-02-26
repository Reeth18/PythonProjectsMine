'''Problem Statement :
You are required to build a custom application in python and this application will work in the following ways :
You are required to take two inputs from the user.
Now the first functionality of the application will be to check if the given two inputs are numbers or not. if it is a number, you are required to do other tasks of the application, and if not a number, inform the user to input numbers only.
Now if the inputs are in numbers, check whether the given numbers are even or odd .
If Odd , you have to print the product of the number.
If Even, you have to print the sum of the number.
Lastly, you also have to check whether any of the numbers given as input are prime numbers or not.'''
#Taking Two Inputs from the User
userInput1 = int(input("Enter the Number: ")) 
userInput2 = int(input("Enter the Number: ")) 
#Now checking the type of the User Inputs
print(type(userInput1))
print(type(userInput2))

#Checking the Number (Odd or Even) and (Prime or Composite) Number.
#First Checking Odd or Even
#Case1 : Both are Even Numbers
if (userInput1%2 == 0 and userInput2%2 == 0):
    print(userInput1, " and ", userInput2, " are Even Numbers.")
    sumOfNumbers = (userInput1 + userInput2)
    print("Sum of the Two Even Numbers is:", sumOfNumbers)#Printing Sum when both the numbers are Even

#Both are Odd Numbers    
elif (userInput1%2 != 0 and userInput2 != 0):
    print(userInput1, " and ", userInput2, " are Odd Numbers.")
    productOfNumbers = (userInput1 * userInput2)
    print("Product of the Two Odd Numbers is:", productOfNumbers)#Printing Product when both the numbers are Even
    
#Number 1 is Even and Number 2 is Odd
elif (userInput1%2 == 0 and userInput2 != 0):
    print(userInput1, "is an Even Number and ", userInput2, " is an Odd Number.")

#Number 1 is Odd and Number 2 is Even
elif (userInput1%2 != 0 and userInput2 == 0):
    print(userInput1, "is an Odd Number and ", userInput2, " is an Even Number.")
    
#Now Checking if a Number among the two Numbers is prime or not

if (userInput1 > 1):
    for index in range(2, userInput1):
        if(userInput1 % index != 0):
            print(userInput1, "is a Prime Number.")#If the Number is only divisible by 1 and itself it is a Prime No. Eg: 2,3,5,7........
            break
        else:
            print(userInput1, "is not a Prime Number.")#If the Number is divisible by atleast 2numbers other than One and Itself it is a Composite Number. Eg:4,6,8,9,.........
            break
        
else:
    print(userInput1, "is not a Prime Number.")#Any Number <= 1 is not a Prime Number as it does not satisfy the defintion of Prime Numbers. Eg:1,0,-1,-2,............,-nterms
