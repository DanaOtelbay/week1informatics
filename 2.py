import re
s = input()
ans = re.search(r"[A-Z][a-z]+", s)
if ans:
   print("YES")
else:
   print("NO")