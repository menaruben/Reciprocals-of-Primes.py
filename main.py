import math
import string

def main(n): # n mustn't be 2 or 5
    # https://en.wikipedia.org/wiki/Reciprocals_of_primes - inspired by William Shanks
    k = 0

    oop = 1/n
    BOOL = False

    while BOOL == False:
        if n > 10**k and n < 10**(k+1):
            #nz = k
            BOOL = True

        else:
            k += 1
    
    # loop-length
    r = [10**(k+1)]
    Loop = False
    i = 0

    while Loop == False:
        if i == 0:
            rs = (r[0]%n)*10
            r.append(rs)

            if r[1] == r[0]:
                return i
                Loop = True
            else:
                i += 1
        
        elif i != 0:
            rs = (r[i]%n)*10
            r.append(rs)

            if r[i] == r[0]:
                return i
                Loop = True
            else:
                i += 1

print(main(7))