from re import *
# with open("given.txt", "r") as f:
#    line = f.read()
# text = search(r"([^\n]+)\n", line).group(1)
# t = search(r"\n([^\n]+)\n", line).group(1)
# s = search(r"\n([^\n]+)\n([^\n]+)\n", line).group(2)
# f = search(r"\n([^\n]+)", line).group(1)
# text.replace(t, s)
# ans = findall(f, text)
# print(len(ans))
text = input()
t = input()
s = input()
f = input()
new_text = text.replace(t, s)
ans = findall(f, new_text)
print(len(ans))