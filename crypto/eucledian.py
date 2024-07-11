def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def e_eucledian_gcd(a, b):
    a,b,t1,t2=a,b,0,1
    while b!=0:
        q,r=a//b,a%b #floor division and remainder
        t1,t2=t2,t1-q*t2
        a,b=b,r
    return a


x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))

print(f"The gcd of the two numbers using eucledian  is: {gcd(x,y)} and extended eucledian is {e_eucledian_gcd(x,y)}" )