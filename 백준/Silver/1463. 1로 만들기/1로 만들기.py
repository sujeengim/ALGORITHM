import sys
n= int(sys.stdin.readline())
dp = [0] * (n+1) #1~n의 최소 연산 횟수 저장, 0~1은 0회임

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 #세 연산 중 아무때나 가능한 -1을 한 경우로 우선 기준을 잡아두기 
    # 기준 잡아두고 이제 판단해보기 
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1) #2로 나누는게 더 적은 연산 횟수라면 갱신
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1) #3으로 나누는게 더 적은 연산 횟수라면 갱신

print(dp[n])
