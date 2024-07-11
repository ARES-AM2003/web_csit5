from math import gcd
n=int(input("Enter the number: "))

def relatively_prime(n):
    relatively_prime_list=[]
    for i in range(1,n):
        if gcd(i,n)==1:
            relatively_prime_list.append(i)
    return relatively_prime_list

print(f"The Phi({n}) is {len(relatively_prime(n))}")