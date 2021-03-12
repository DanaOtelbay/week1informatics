a, d = map(int, input().split())
year = 0
while d>=a:
   a *= 3
   d *= 2
   year += 1

print(year)