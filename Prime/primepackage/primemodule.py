'''These are defined functions that will
    do work on the input from the generate.py file
'''

__author__= "Tamikal Johnson"
__license__=""
__version__=""
__email__="tamijohnson@valdosta.edu"
__status__="DONE"

def isPrime(n):
    '''This function checks if the number given.
        is a prime number.
        Args:
            Number (int):input
        Returns:
            Boolean (True or False)
        This is for the getNPrime function and is the
        boolean condition that runs the loop.
    '''
    if(n==1):
        return False
    elif(n==2):
        return True
    else:
        for x in range(2,n//2+1):
            if(n%x==0):
                return False
        return True

def getNPrime(n):
    '''This function takes the input and puts it into a list.
        When the while loop is done putting the numbers into the
        list it will return the list.
    
        Args:
            Number (int):input
        Returns:
            Array (list):output
    '''
    plist=[]
    num=1

    while len(plist)<n:
        if isPrime(num)==True:
            plist.append(num)
        num = num + 1
    return plist

    
