from datetime import datetime, timezone, timedelta

print(datetime.now())

# UTC is the global time followed across the globe
print(datetime.now(timezone.utc))

today = datetime.now()
tomorrow = today + timedelta(days=1)

print(today, tomorrow)

# For formatting to different date time format
# 07-05-2022 18:14
print(today.strftime('%d-%m-%Y %H:%M:%S'))

user_date = input('Enter the date in YYYY-mm-dd format:')

# Appends the time to the date part
# 2020-05-03 00:00:00
user_date = datetime.strptime(user_date, '%Y-%m-%d')

print(user_date)






