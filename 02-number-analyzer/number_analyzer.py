n=int(input("Enter the number: "))
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def sum_digit(n):
    return sum(int(d) for d in str(abs(n)))


def analyzer(n):
    if n>0:
        print("The number is positive")
    elif n<0:
        print("The number is negative")
    else:
        print("The number is zero")
    if n%2==0:
        print("The nuumber is even")
    else:
        print("The number is odd")
    if is_prime(n):
        print("The number is a prime number")
    else:
        print("The number is not prime")
    dsum=sum_digit(n)
    print("Sum of digits is:",dsum)

    if is_prime(dsum):
        print("The sum of digit is prime number")
    else:
        print("The sum of digit is not prime")
analyzer(n)
