import datetime

given_date = input("Enter a given date in the format DD-MM-YYYY: \n")
given_date = list(given_date)

given_day = ''.join(given_date[0:2])
given_month = ''.join(given_date[3:5])
given_year = ''.join(given_date[-4:])

current_date = list(str(datetime.datetime.now()))
current_year = ''.join(current_date[0:4])
current_month = ''.join(current_date[5:7])
current_day = ''.join(current_date[-2:])

year_difference = int(current_year) - int(given_year)
month_difference = int(current_month) - int(given_month)
day_difference = int(current_day) - int(given_day)

if month_difference <= 0:
    if day_difference >= 0:
        print('Age: ' + str(year_difference - 1))
else:
    print('Age: ' + str(year_difference))
