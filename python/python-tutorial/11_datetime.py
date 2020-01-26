# Datetime module

# === Date ===
import datetime
toda = datetime.date.today()
new_year = datetime.date(2030, 1, 1)

# === Time ===
noon = datetime.time(12, 0, 0) # time(12)

# === Date and Time ===
now = datetime.datetime.now()

# === Parsing ===
millenium = datetime.datetime(2000, 1, 1, 0, 0, 0)


# === Operations ===
# Do this instead
print('Time since the millenium at midnight: ', datetime.datetime(today.year, today.month, today.day) - millenium_turn)

# Or this
print('Time since the millenium at noon: ', datetime.datetime.combine(today, noon) - millenium_turn)


# === Timezones ===
# By default, datetime are naive. To make timezone-aware we need to provide tzinfo

# Japan timezone
JST = datetime.timezone(datetime.timedelta(hours=+9))

dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)
print(dt) # 2015-01-01 12:00:00+09:00
print(dt.tzname()) # UTC+09:00

dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=timezone(timedelta(hours=9), 'JST'))
print(dt.tzname) # 'JST'

now = datetime.now()
then = datetime(2016, 5, 23)
delta = now - then

print(delta.days) # 60
print(delta.seconds) # 40826

ten_days_from_now = datetime.datetime.now() + datetime.timedelta(days=10)
yesterday = datetime.datetime.now() - datetime.timedelta(days=-1)

# Switching between timezones
from dateutil import tz

utc_now = datetime.datetime.utcnow()
print(utc_now) # not timezone-aware

utc_now = utc_now.replace(tzinfo=tz.tzutc())
print(utc_now) # timezone-aware

local_now = utc_now.astimezone(tz.tzlocal())


# === Parsing ===

# ISO 8601
import iso8601
so8601.parse_date('2016-07-22 09:25:59') # datetime.datetime(2016, 7, 22, 9, 25, 59, tzinfo=<iso8601.Utc>)
iso8601.parse_date('2016-07-22 09:25:59+03:00') # datetime.datetime(2016, 7, 22, 9, 25, 59, tzinfo=<FixedOffset '+03:00' ...>)
iso8601.parse_date('2016-07-22 09:25:59Z') # datetime.datetime(2016, 7, 22, 9, 25, 59, tzinfo=<iso8601.Utc>)
iso8601.parse_date('2016-07-22T09:25:59.000111+03:00') # datetime.datetime(2016, 7, 22, 9, 25, 59, 111, tzinfo=<FixedOffset '+03:00' ...>)


datetime.now().isoformat() # '2016-07-31T23:08:20.886783'
datetime.now(tz.tzlocal()).isoformat() # '2016-07-31T23:09:43.535074-07:00'


# Fuzzy
from dateutil.parser import parse
dt = parse("Today is January 1, 2047 at 8:21:00AM", fuzzy=True)
print(dt)


# === Iterating ===
import datetime

day_delta = datetime.timedelta(days=1) # The size of each step in days
start_date = datetime.date.today()
end_date = start_date + (7 * day_delta)

for i in range((end_date - start_date).days):
    print(start_date + i*day_delta)
