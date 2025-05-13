import calendar

clndr=calendar.month(2025,4)
print(clndr)
import datetime
today=datetime.date.today()

print(today)
yes=today - datetime.timedelta(days=1)
print(yes)
yes1=today - datetime.timedelta(days=2)
print(yes1)
from datetime import datetime
now=datetime.now()
print(f"time is {now}")