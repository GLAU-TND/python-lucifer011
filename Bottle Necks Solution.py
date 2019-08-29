#
#@author AnushkaSoni
#@username lucifer011
#@version 1.0
#
n = int(input())
lst = list(map(int,input().split(" ")))
fill=[]
for i in range(0,n):
    fill.append(lst.count(i))

print(max(fill))