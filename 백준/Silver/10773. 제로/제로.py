import sys

k = int(sys.stdin.readline().strip())
klist = []

for i in range(k):
    n = int(sys.stdin.readline().strip())

    try:
        if n < 0:
            raise ValueError
        if n == 0:
            # pop
            del klist[-1]
        else :
            # push
            klist.append(n)
    except ValueError:
        pass

print(sum(klist))
