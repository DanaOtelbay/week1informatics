s = input().split('-')
word_even = []
print(s)
for word in s:
   if len(word)%2==0:
      word_even.append(word)
word_even.sort()
print(*word_even)
