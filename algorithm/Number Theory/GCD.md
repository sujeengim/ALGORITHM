## 유클리드 호제법

유클리드 호제법은 두 양의 정수 또는 다항식의 
<b>최대공약수(GCD, Greatest Common Divisor)</b>를 구하는 가장 오래되고 효율적인 알고리즘이다.

> 두 정수 $a$와 $b$ ($a > b$)의 최대공약수는 $b$와 $a$를 $b$로 나눈 나머지 $r$의 최대공약수와 같다.

> $$\text{GCD}(a, b) = \text{GCD}(b, r)$$
> 
> (여기서 $r = a \pmod{b}$)

즉, 큰 수 $a$와 작은 수 $b$의 최대공약수를 구하는 문제가 $b$와 $r$이라는 더 작은 두 수의 최대공약수를 구하는 문제로 단순화 된다. 


```python
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
```


- 여러 수의 최대공약수 구하기 : 두 수씩 묶어 순차적으로 GCD
```python
gcd_value = newlist[0]
for i in range(1, len(newlist)):
    gcd_value = gcd(gcd_value, newlist[i])
```
