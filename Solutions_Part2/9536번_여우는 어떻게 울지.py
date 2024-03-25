import sys
n=int(input())
sounds=[]

for _ in range(n):
    line=sys.stdin.readline()
    sounds.append(line.split())    
    l=[]
    while 1 :
        sound_ani=sys.stdin.readline().rstrip('\n')
        if sound_ani=='what does the fox say?': break
        l.append(sound_ani.split())

    for i in range(len(l)):
        l[i]=l[i][2]
    sounds.append(l)

for i in range(0,len(sounds),2):
    result=''
    for j in sounds[i]:
        if j not in sounds[i+1]:
            result+=(j+' ')
    print(result.rstrip('\n'))
