S = input()
total_sum = 0
star_index = -1 # 인덱스 0도 유효하므로 -1로 초기화

for i, s in enumerate(S):
    if s == '*':
        star_index = i
        continue
        
    num = int(s)
    
    # i가 짝수 인덱스(0, 2, 4...) -> 가중치 1
    # i가 홀수 인덱스(1, 3, 5...) -> 가중치 3
    if i % 2 == 0:
        total_sum += num * 1
    else:
        total_sum += num * 3

# 총합이 10의 배수가 되어야 하므로, 필요한 나머지 K를 계산합니다.
# K = (10 - total_sum) % 10. (0부터 9 사이의 값을 확실히 얻기 위해)
K = (10 - (total_sum % 10)) % 10

if star_index % 2 == 0:
    # 1. 별표(*)가 가중치 1 자리에 있을 때 (1X + sum = 0 mod 10)
    # X = K mod 10
    print(K) 
else:
    # 2. 별표(*)가 가중치 3 자리에 있을 때 (3X + sum = 0 mod 10)
    # 3X = K mod 10. 해는 X = 7K mod 10 입니다.
    # 3과 7의 곱이 21이고 21 mod 10 = 1이기 때문에 7을 곱함
    result_x = (K * 7) % 10 
    print(result_x)