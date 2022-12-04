'''
You are then going to create a function called days_in_month() which will take a year and a month as inputs, 
And it will use this information to work out the number of days in the month, then return that as the output
'''
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month>12 or month<1:
    return "invalid input"  
  leap_year = is_leap(year)
  if month == 2 and is_leap(year)==True:
    return 29
  return month_days[month-1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
