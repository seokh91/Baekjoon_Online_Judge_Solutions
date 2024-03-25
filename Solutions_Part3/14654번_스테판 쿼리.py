import sys

def judge(a,b,cnt_a,cnt_b):
    if a=='1' and b=='3' :
        return a
    elif a=='3' and b=='1' :
        return b
    elif a > b :
        return a
    elif a < b :
        return b
    elif a==b :
        if cnt_a==0 : return 'a'
        elif cnt_b==0 : return 'b'

if __name__=="__main__":
    n=int(input()) ; cnt_a=0 ; cnt_b=0 ; max_cnt=0
    rounds_a=sys.stdin.readline().rstrip('\n').split()
    rounds_b=sys.stdin.readline().rstrip('\n').split()

    while len(rounds_a)!=0 and len(rounds_b)!=0 :
        if rounds_a[0] == rounds_b[0] :
            if judge(rounds_a[0],rounds_b[0],cnt_a,cnt_b)=='a':
                cnt_a+=1 ; cnt_b=0 ; rounds_a.pop(0) ; rounds_b.pop(0)
            else :
                cnt_b+=1 ; cnt_a=0 ; rounds_a.pop(0) ; rounds_b.pop(0)
        else :
            if judge(rounds_a[0],rounds_b[0],cnt_a,cnt_b)==rounds_a[0]:
                cnt_a+=1 ; cnt_b=0 ; rounds_a.pop(0) ; rounds_b.pop(0)
            else : cnt_b+=1 ; cnt_a=0 ; rounds_a.pop(0) ; rounds_b.pop(0)

        if max_cnt < cnt_a or max_cnt < cnt_b : max_cnt=max((cnt_a, cnt_b))

    print(max_cnt)
