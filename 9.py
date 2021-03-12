s = list(map(str, input().split()))
d = dict()
for word in s:
   d[word]=len(word)

len = list(d.values())
max = -1111
for n in len:
   if n>max:
      max=n

for word in d:
   if max == d[word]:
      print(word)
      print(max)
      break