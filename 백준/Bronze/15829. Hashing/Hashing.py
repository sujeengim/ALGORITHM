import sys

abc = {v:idx+1 for idx,v in enumerate("abcdefghijklmnopqrstuvwxyz")}

def r31(input):
    sum = 0
    for idx, i in enumerate(input):
        sum += 31**idx * abc[i]
    return sum

n = int(input())
input_string = sys.stdin.readline().strip()
print(r31(input_string))
