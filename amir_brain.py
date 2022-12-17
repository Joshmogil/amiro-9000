from datetime import datetime
import holidays

# Select country
us_holidays = holidays.US()
today_str = datetime.today().strftime('%m-%d-%Y')
now = datetime.datetime.now()


print(today_str)

holiday = us_holidays.get('1-17-2022')
holiday = holiday if holiday not in ["Christmas Day (Observed)", "Juneteenth National Independence Day (Observed)"] else False

for ptr in holidays.US(years = int(today_str.split('-')[2])).items():
    print(ptr)


print(now.isoweekday())

def determine_prompt(holiday,now):
    print(now.isoweekday())