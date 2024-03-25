import sys
while True:
    line=sys.stdin.readline().rstrip()
    if line=='.':break
    length=len(line)
    if length%2!=0:length+=1
    i=0; check=False
    for i in range(1,length//2+1):
        if length%i==0 :
            what=line[0:i]; temp=length//i 
            if what*temp == line :
                print(length//i); check=True; break
    if i==length//2 and not check: print(1)
