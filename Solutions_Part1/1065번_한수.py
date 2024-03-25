n=int(input())

def hansoo (num):
    if num<=99:
        return num
    elif num>=100 and num<1000:
        cnt=99
        for i in range(100, num+1):
            l=list(map(int, list(str(i))))
            if (l[1]-l[2]) == (l[0]-l[1]): cnt+=1
        return cnt
    elif num==1000:
        return hansoo(999)

print(hansoo(n))
