a = list(map(int, input().split()))
b = list(map(int, input().split()))
t = int(input())
ans = zip(a, b)
wet = 0
for x, y in ans:
   if x<=t<=y:
      wet+=1

print(wet)