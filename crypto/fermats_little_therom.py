p=int(input('ehter a prime number: '))
a=int(input('enter a positive integer which is not divisivle by p: '))
from math import pow

# a^p-1 is congurnt to 1 (mod p)


# check condition
def check_condition(p,a):
    if (a>0 and a%p==0):
        print("not a valid choice")
        a=int(input('enter a positive integer which is not divisivle by p: '))
        fermat_little(p,a)
        
    elif(a<1):
        print("not a valid choice")
        a=int(input('enter a positive integer : '))
        fermat_little(p,a)
        
    else:
        return True
    
def fermat_little(p,a):
    if check_condition(p,a):
        p_new=int(pow(a,p-1))
        
        if p_new%p==1:
            print(f"The fermat little theorem is true for prime number {p}  and a number {a}")
        else:
            print("The fermat little theorem is false")
    
fermat_little(p,a)

        
