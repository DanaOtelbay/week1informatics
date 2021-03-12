import re
year, month, day = input().split()
if re.search(r"\d{4}", year):
   if re.search(r"\d{2}", month):
      if re.search(r"\d{2}", day):
         if 1299<=int(year)<=1922:
            if 1<=int(month)<=12:
               if 1<=int(day)<=31:
                  print("Yes")
               else:
                  print("No")
            else:
               print("No")
         else:
            print("no")
      else:
         print("No")
   else:
      print("No")
else:
   print("No")     