a = list(map(int, input().split()))
n = int(input())
ans = []
for i in range(1, max(a)+1):
   for j in a:
      boo = 0
      if i == j:
         boo = 1
         break
   if boo == 0:
      ans.append(i)
for i in range(1, len(ans)+1):
   if i == n:
      print(ans[i-1])