import re
s = input().split()
k = int(input())
l = []
for i in range(k):
   ss= input()
   l.append(ss)
for i in range(k):
   ll = []
   for j in range(len(s)):
      a = re.search(r"^("+l[i].lower()+")", s[j].lower())
      if a:
         ll.append(s[j])
      # if l[i].lower() in s[j].lower():
      #    ll.append(s[j])
   print(*ll)