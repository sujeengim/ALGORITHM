'''
새로 정한 균일 간격 g -> 현재 "간격"들과 g는 배수 관계
-> g는 현재 간격들의 공약수임
ex. "간격"들이 아래와 같다면
1 | 2 | 4 | 6 | 8 | 10 => 약수를 구해보자 => 
1, (1,2), (1,2,4), (1,2,3,6), (1,2,4,8), (1,2,5,10) => 공약수인 1,2가 간격 g 후보가 됨.
=> g씩 점프하다 보면 언젠가 위치에 정확히 도달해야 하기 때문
-> 최소한의 나무를 심기 위해서 g는 현재 간격들의 최대공약수여야 함 -> 최종 g=2
'''

import sys
n = int(input())
nlist = []
for _ in range(n):
    nlist.append(int(sys.stdin.readline().strip()))
newlist = []

# 1. 간격 리스트 생성
for i in range(len(nlist)-1):
    newlist.append(nlist[i+1]-nlist[i])

# 2. 최대공약수 함수(유클리드 호제법)
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

# 3. 여러값의 최대공약수 계산
gcd_value = newlist[0]
for i in range(1, len(newlist)):
    gcd_value = gcd(gcd_value, newlist[i])

# 4. 필요한 나무 수 - 기존 나무 수
ans = (nlist[-1] - nlist[0]) // gcd_value + 1 - n
print(ans)

