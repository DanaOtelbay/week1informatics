s = input()
a, b = map(int, input().split())
x=0
y=0
wet = 1
for i  in s:
   if x == a and y == b:
      print("Passed")
      wet = 0
      break
   if i == "L":
      x-=1
   elif i == "R":
      x+=1
   elif i == "U":
      y+=1
   elif i == "D":
      y-=1
   if x == a and y == b:
      print("Passed")
      wet = 0
      break
if wet == 1:
   print("Missed")