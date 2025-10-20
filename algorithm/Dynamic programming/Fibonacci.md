### 직관적인 중복호출
- 시간복잡도 : O(2**N)
```python
n = int(input())

def fib(n):
  if n==0 or n==1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

print(fib(100))
```
=> 계산이 평생 되지 않음

<hr>

### (개선)시간 단축을 위한 재활용 방법
- 시간복잡도 : O(N)
```python
n = int(input())
f = [0 ]*n

def fibo(n):
  if f[n] != 0: #이 위치에 저장된 값이 있다면 또 계산 말고 가져오기 
    return f[n]
  else:
    if f[n] == 0 or f[n] == 1 :
      f[n] = 1
    else:
      f[n] = fibo[n-1] + fibo[n-2]

print(fibo(100))
```
