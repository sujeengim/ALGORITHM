import sys

s = set()

def commands(command:list):
    global s 

    cmd = command[0]
    num = int(command[1]) if len(command) > 1 else None 

    if cmd == 'add':
        s.add(num) 
    elif cmd == 'remove':
        
        if num in s:
            s.remove(num) 
    elif cmd == 'check':
        print(1 if num in s else 0)
    elif cmd == 'toggle':
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif cmd == 'all':
        s = set(range(1,21)) 
    elif cmd == 'empty':
        s.clear() 
 
def main():
    m = int(input())

    for _ in range(m):
        command = sys.stdin.readline().strip().split()

        if command[0] == 'all' or command[0] == 'empty':
            commands(command)
        else:
            commands(command)

if __name__ == "__main__":
    main()