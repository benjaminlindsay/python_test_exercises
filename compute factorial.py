# Question 2:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)

x=int(input("Input a number to compute: "))

print (fact(x))

# NOTES
#The input() function allows user input from the console.
#int() Return an integer object constructed from a number or string x, or return 0 if no arguments are given.
#If x is a number, it can be a plain integer, a long integer, or a floating point number.
#If x is floating point, the conversion truncates towards zero.
#If the argument is outside the integer range, the function returns a long object instead.
