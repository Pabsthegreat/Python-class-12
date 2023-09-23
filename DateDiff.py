from datetime import date
date1=date(int(input("Enter the year of the first date: ")),int(input("Enter the month of the first date: ")),int(input("Enter the day of the first date: ")))
date2=date(int(input("Enter the year of the second date: ")),int(input("Enter the month of the second date: ")),int(input("Enter the day of the second date: ")))
delta = date2 - date1
print(delta.days)
