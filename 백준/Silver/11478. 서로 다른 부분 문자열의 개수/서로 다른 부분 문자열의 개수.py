S = input()
sset = set()
for i in range(1,len(S)+1):
    for j in range(len(S)-i+1):
        sset.add(S[j:j+i])

print(len(sset))