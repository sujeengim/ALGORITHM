N = int(input())
step_score = [0] + [int(input()) for _ in range(N)] #계단별 점수 저장
if N<3:
    if N==1:
        print(step_score[1])
    else:
        print(step_score[1]+step_score[2])
else:
    # [연속 경우 최대값, 점프 경우 최댓값]
    dp = [[0, 0] for _ in range(N + 1)]
    
    # 기저값 설정
    dp[1] = [step_score[1], step_score[1]]
    dp[2] = [step_score[1] + step_score[2], step_score[2]]

    for i in range(3, N+1): 
        dp[i][0] = dp[i-1][1] + step_score[i] #삼중연속 불가 라서 바로 [1] 가져오기 
        dp[i][1] = max(step_score[i] + dp[i-2][0], \
                    step_score[i] + dp[i-2][1])

    print(max(dp[N][0], dp[N][1]))
