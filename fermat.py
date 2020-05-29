#a^k mod p

def returnMod(a,k,prime):
    reduced = k % (prime-1)
    return (a**reduced) % (prime)
    #maybe when the numbers get big enough this has to be changed

def main():
    print(returnMod(3,1353,17))

main()
