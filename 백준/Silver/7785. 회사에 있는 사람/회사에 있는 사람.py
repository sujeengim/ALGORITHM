import sys

nowSet = set()

for _ in range(int(input())):
    whowhat = sys.stdin.readline().split() # 문자열 리스트로 생성
    if whowhat[1] == 'enter':
        nowSet.add(whowhat[0]) # 첫번째 요소를 set에 추가
    elif whowhat[1] == 'leave':
        nowSet.remove(whowhat[0])
    else:
        pass

# set은 정렬되지 않으므로, 자체로 역순 출력 불가 -> list로 변환하기 
# 리스트 생성과 정렬 작업을 분리해야 합니다.
nowList = list(nowSet)
nowList.sort(reverse=True) # 사전순 역순
print(*(nowList), sep='\n') 