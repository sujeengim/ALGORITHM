import sys
from collections import Counter

# 1. 입력 처리: 한 줄로 끝내고, nlist는 이미 정렬되어 있음
N = int(sys.stdin.readline())
nlist = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])

# 2. 산술평균 (소수점 첫째 자리에서 반올림)
# 파이썬 내장 round() 사용
avg = round(sum(nlist) / N)
print(avg)

# 3. 중앙값
mid_value = nlist[N // 2]
print(mid_value)

# 4. 최빈값 (가장 효율적인 방식)
cnt = Counter(nlist) # 각 숫자의 빈도수를 딕셔너리 형태로 저장
max_count = max(cnt.values()) 

# 최대 빈도수와 동일한 값을 가진 요소(키)들을 리스트로 모읍니다.
modes = [k for k, v in cnt.items() if v == max_count]

if len(modes) > 1:
    # 최빈값이 여러 개일 경우: 정렬하여 두 번째로 작은 값 출력
    modes.sort()
    print(modes[1]) # 정렬된 리스트의 1번 인덱스 (두 번째 작은 값)
else:
    # 최빈값이 하나일 경우: 유일한 값 출력
    print(modes[0])

# 5. 범위
range_value = nlist[-1] - nlist[0]
print(range_value)