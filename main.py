def fact_rec(n):
   if n==0 or n==1:
      return 1
   else:
      return n*fact_rec(n-1)

number =int(input("ENTER A VALUE:"))
res=fact_rec(number)

print("The factorial of {} is {}".format(number, res))
"""  year % 4 == 0 &
year % 100 != 0 /
year % 400 == 0  """


def isleapyear(year):
  if( year  % 4 == 0 and year  % 100 != 0) or year  % 400 ==0:
     return True
  else:
     return False

year= int(input("Enter a year:"))

if isleapyear(year):
  print("{} is leap year.".format(year))
else:
  print("{} is not a leap year. ".format(year))