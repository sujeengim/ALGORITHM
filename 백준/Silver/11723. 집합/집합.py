import sys

s = set()

def commands(command:list):
    global s

    cmd = command[0]
    if cmd == 'add':
        s.add(int(command[1]))
    elif cmd == 'remove':
        if int(command[1]) in s:
            s.remove(int(command[1]))
    elif cmd == 'check':
        print(1 if int(command[1]) in s else 0)
    elif cmd == 'toggle':
        if int(command[1]) in s:
            s.remove(int(command[1]))
        else:
            s.add(int(command[1]))
    elif cmd == 'all':
        s = set(range(1,21))
    elif cmd == 'empty':
        s.clear()
    else:
        pass

def main():
    m = int(input())

    for _ in range(m):
        command = sys.stdin.readline().strip().split()
        commands(command)

if __name__ == "__main__":
    main()
