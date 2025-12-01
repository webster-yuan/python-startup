songlist={}
n=int(input())
max=0
for i in range(n):
    songlist[i]=list(input().split())
for i in range(0,n-1):
    for j in range(i+1,n):
        if int(songlist[i][2])>int(songlist[j][2]):
           songlist[i],songlist[j]=songlist[j],songlist[i]
           
for i in range(n):
    print(songlist[i][0],songlist[i][1],songlist[i][2])