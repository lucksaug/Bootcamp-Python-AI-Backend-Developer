from datetime import datetime, timezone, timedelta
# ? PYTZ
# import pytz as tz

# data = datetime.now(tz.timezone('Europe/Oslo'))
# print(data)
# data = datetime.now(tz.timezone('Etc/UTC'))
# print(data)

# ? datetime.timezone
data_oslo = datetime.now(timezone(timedelta(hours=2), name="Oslo"))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3), name="São Paulo"))
print(data_oslo)
print(data_sao_paulo)