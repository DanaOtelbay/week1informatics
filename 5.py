n = input().split()
a = set(n)
l=list(a)
c=0
for i in range(len(l)):
   x=n.count(l[i])
   for j in range(x):
      c+=j
print(c)