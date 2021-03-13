s1 = set(input().split())
s2 = set(input().split())
ans = []

a = s1.difference(s2)
a = list(a)
b = s2.difference(s1)
b = list(b)
for i in a+b:
      print(i, end= " ")