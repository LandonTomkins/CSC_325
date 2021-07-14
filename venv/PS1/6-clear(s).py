S = []

for i in range(0,10):
    S.append(i)

def clear(S):
    if len(S) > 0:
        S.pop()
        clear(S)

print(S)
clear(S)
print(S)