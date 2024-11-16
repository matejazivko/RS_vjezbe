#1
def isPrime(broj):
    if broj > 1:
        for i in range(2,broj):
            if(broj % i) == 0:
                print("False")
                break
        else:
            print("True")
    else:
        print("False")
print (isPrime(10))

#2
def primes_in_range(start, end):
    lista=[]
    for i in range (start, end):
        if isPrime(i):
            lista.append(i)
    return lista

print(primes_in_range(1,10))