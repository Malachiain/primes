

def testnumber(nu):
    factors = findfac(nu)
    #the power which two is rasied to
    s = factors[0]
    #the odd factor
    d = factors[1]
    # this is the bases that will be checked
    bases = [2,3,5,7,11]
    for a in bases:
        if checkbase(a,s,d, nu):
            print(str(nu)+" is composite with witness "+str(a))
            return False
    
    print(str(nu)+" is probably prime")    
"""
check if the current base is a witness
returns true if it is a witness
"""
def checkbase(a,s,d, n):
    ad = (a**d)%n
    if ad ==1:
        return False
        
    for r in range(0,s):
        twor = 2**r
        p = int(a)**int(twor*d)
        mod = p%n
        
        #print("base "+str(a) + " 2^r*d "+str(n)+" power "+ str(r)+" result "+str(mod))

        if mod == n-1:
            return False
    return True

def findfac(number):
    if number%2 ==0:
        print(str(number)+" is not prime as it is even")
    
    power = 0
    oldnumber =0
    newnumber = float((number-1) /2)

    while newnumber.is_integer():
        power = power + 1
        oldnumber = newnumber
        newnumber = newnumber/2
    oddnumber = oldnumber
    print(str(number)+ "-1 can be expressed as 2^"+str(power)+"*"+str(oddnumber))
    return (power, oddnumber)

def main():
    inp = int(input("enter a number to test: "))
    testnumber(inp)

if __name__ == "__main__":
    main()

        
    