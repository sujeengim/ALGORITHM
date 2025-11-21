```python
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = prices[-1]
    sum_price = 0

    for i in range(N-2, -1, -1):
        current_price = prices[i]
        if (current_price < max_price):
            sum_price += (max_price-current_price)
        elif (current_price >= max_price):
            max_price = current_price

    print(f'#{test_case} {sum_price}')
```

https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1

1859. 백만 장자 프로젝트

# greedy 탐욕 알고리즘 
- 원리 : 매순간 가장 최적의 선택을 하여 최종으로 전체적인 최적 해를 구함
- 현재 시점에서 봤을 때 가장 이득의 선택을 한다. (바로 눈앞의 이득을 쫓는다)

max_price가 고정되어 있으니 이보다 작은 값이 나올때마다 이득을 누적하고

이보다 큰 값이 나오면 max_price를 갱신한다.

파는 것은 산 날 보다 이후에 팔기에 

for 문에서 인덱스를 반대로 설정한다. 
