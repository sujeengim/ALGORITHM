
S = input()
total_sum = 0
star_index = -1

for i, s in enumerate(S):
    if s == '*':
        star_index = i
        continue
        
    num = int(s)

    weight = 1 if i % 2 == 0 else 3
    total_sum += num * weight

W = 1 if star_index % 2 == 0 else 3

for X in range(10): #0~9까지 확인
    final_sum = total_sum + (X * W)
    if final_sum % 10 == 0:
        print(X)
        break     
