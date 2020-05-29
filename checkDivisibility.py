def compute(p,x,b):
    #computes 2^x (mod p)
    if (x == 0):
        return 1
    elif (x == 1):
        return (int(b)%int(p))
    elif (int(x) % 2 == 1):
        value = compute(p,int(x-1)/2,b**2) % int(p)
        return (b*value)
    else:
        value = compute(p,int(x)/2,b**2) % int(p)
        return value
    #this is the recursive implementation

#i haven't checked if the alternate implementations work yet

"""
alternate implementation for the compute function which should work the same
note: i don't think the b variable is necessary and can just be replaced with 2
i think dynamic programming can optimize this, but this should work fine

def altCompute(p,x,b):
    if (x==0):
        return 1
    else:
        half = compute(p,int(x)//2,b)
        value = half*half
        if (int(x)%2 == 1):
            value *= b
        return (value % p)
"""


"""
here is an attempted implementation of the actual successive squaring method
in which the number (exponent) is written as binary and
we use a precomputed array of powers of 2^(2^n) mod p

def compute(p,x):
    value = 1
    array = [1,2]
    binString = bin(x)
    for i in range(len(binString)-4):
        array[i+2] = (array[i+1]**2) % int(p)

    for i in range(len(binString)-2):
        if (binString[-(i+1)]==1):
            value = (value * array[i]) % int(p)

    return value
"""

def main():
    #note: I am not writing this data to a file
    f = open("pairs.txt","r")
    lines = f.readlines()
    f.close()

    counter = 0
    tracker = 0
    for line in lines:
        newLine = line.strip()
        pair = newLine.split(" ")
        tracker = pair[0]
        if (int(compute(pair[0],int(pair[1])-1,2)) % int(pair[0]) == 1):
            #checks if pair[0]^(pair[1]-1) = 1 (mod pair[0])
            print(pair[0],pair[1])
            counter = 0
        if (counter == 10000): #counter to make sure it's running properly
            print(tracker)
            print("next 10000 failed")
            counter = 0
        counter += 1

    print(tracker)

main()
