a = list(map(int, input().split()))
d = dict()
for i in a:
   if i in d:
      d[i]+=1
   else:
      d[i]=1
sum = 0
for elem in d:
   if d[elem] == 1:
      sum+=elem
print(sum)