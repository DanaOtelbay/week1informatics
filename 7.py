import re
n = int(input())
d = dict()
d["a"]=0
d["b"]=0
d["c"]=0
for x in range(n):
   name,vowels,digits= input().split()

   
   a_f = re.findall(r'[A-Z]6', name)
   b_f = re.findall(r'[aeuioy]', vowels)
   c_f = re.findall(r'[0-9]', digits)
   d["a"]+=len(a_f)
   d["b"]+=len(b_f)
   d["c"]+=len(c_f)
print(d)

# def sec(x):
#    return x[1]

# a=[(1,4),(2,3),(3,2),(4,1)]

# print(sorted(a,key=sec))