# Question 1:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

#Hints: 
#Consider use range(#begin, #end) method

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

solution = ",".join(l)

print(solution)

# NOTES
#The modulus operator works on integers (and integer expressions) and yields the remainder when the
#first operand is divided by the second. In Python, the modulus operator is a percent sign (%).
#The modulus operator turns out to be surprisingly useful. For example, you can check whether one
#number is divisible by another—if x % y is zero, then x is divisible by y. Also, you can extract the
#right-most digit or digits from a number. For example, x % 10 yields the right-most digit of x (in base 10).
#Similarly x % 100 yields the last two digits.
