# d = dict()
# try:
#    while True:
#       name = input()
#       if name in d:
#          d[name]+=1
#       else:
#          d[name]=1
# except:
#    pass
# l_ans = []
# for i in d:
#    if d[i]%2==0:
#       l_ans.append(i)

# l_ans.sort()

# for i in l_ans:
#    print(i)
import re
d={}
with open("input.txt", "r") as f:
   name_line = f.readlines()
for name in name_line:
   if name in d:
      d[name]+=1
   else:
      d[name]=1
l_ans = []
for i in d:
   if d[i]%2==0:
      l_ans.append(i)
l_ans.sort()
for i in l_ans:
   print(i.strip("\n"))
# ans = re.findict(r"")