a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

def gcd(x, y): #최대공약수
    while y:
        x, y = y, x%y
    return x

def lcm(x, y): #최소공배수
    return (x // gcd(x, y)) * y

final2 = lcm(a2, b2) #분모
final1 = a1*(final2//a2) + b1*(final2//b2) #분자

final_gcd = gcd(final1, final2)

print(final1//final_gcd, final2//final_gcd)
