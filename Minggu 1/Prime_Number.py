def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

number = int(input("Masukkan nilai : "))

for i in range(1,number+1):
    if(isPrime(i)):
        print(i,end=" ")