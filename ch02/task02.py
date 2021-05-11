from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')

time = datetime.now(JST)

print(time)
print(time.hour)