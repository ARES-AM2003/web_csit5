def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False
def prime_range(start, end):
    primes = []
    for num in range(start, end+1):
        if num > 1:
            if num==2 or num==3:
                primes.append(num)
            else:
               

                if check_prime(num):
                    primes.append(num)
                    

                # for i in range(2,num):
                #     if (num % i) == 0:
                #         break
                # else:
                #     primes.append(num)
    return primes
if (__name__ == "__main__"):
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    print(f"the prime in range {x}, {y} are {prime_range(x,y)}")

    print(check_prime(15))
    print(15%3)
