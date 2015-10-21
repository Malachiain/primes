"""This is an implimentation of a primality test bassed on Fermat's 
little therom. The purpose was to help me remember if for a cryptography exam"""

import fractions as frac

def isprime(number):
    p = number
    minus = p-1 # the number minus 1, the power that it will raised to
    #first check using 2, it will rule out a great deal of compisite numbers
    if not test(2, minus):
        print(str(number)+" is compisite")
        return False
    #check with 3 numbers coprime to n all numbers with less than 3 numbers
    #coprime to them will have already failed the first test
    lastnumber = 2
    for i in range(0,3):
         cop = coprime(lastnumber,number)
         if not test(cop, minus):
             print(str(number)+" is compisite")
             return False
         lastnumber = cop
    #the number has not failed the tests, probably prime
    print(str(number)+" is probably prime")
    return True 
        
    
#if the result is not 1 mod n then the number is compisite
def test(number, power):
    mod = (number**power)%(power+1)
    return mod == 1
"""
find a number coprime to the number being checked
that is larger than the last coprime found
"""    
def coprime(start, number):
    for i in range(start +1, number):
        if frac.gcd(i,number) == 1:
            return i
    #shouldn't reach here
    raise ArithmeticError("Ran out of coprimes")

def main():
    number = int(input("Enter a number to check: "))
    isprime(number)

if __name__ == "__main__":
    main()
