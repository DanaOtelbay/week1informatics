import re
s = input()
c = input()
l = []
for i in range(len(s)):
   if c == s[i]:
      l.append(i)
ans = []
for i in range(len(l)-1):
   for x in range(len(s)):
      if abs(l[i]-x)<abs(l[i+1]-x):
         ans.append(abs(l[i]-x))
      else:
         ans.append(abs(l[i+1]-x))

print(ans)

