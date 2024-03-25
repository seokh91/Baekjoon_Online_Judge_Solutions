import sys

word=sys.stdin.readline().rstrip()
result=set()

for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        result.add(word[i:j])

print(len(result))
