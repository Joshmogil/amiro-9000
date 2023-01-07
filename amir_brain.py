from datetime import datetime
import holidays
import time
from chat_wrap import talk
import random

us_holidays = holidays.US()
today_str = datetime.today().strftime('%m-%d-%Y')
now = datetime.today()

day_enu={
    1:"monday",
    2:"tuesday",
    3:"wednesday",
    4:"thursday",
    5:"friday",
    6:"saturday",
    7:"sunday"
}

def week_enu(week_int):
    if week_int <= 11 or week_int > 47:
        return "winter"
    if week_int <= 23:
        return "spring"
    if week_int <= 35:
        return "summer"
    if week_int <= 47:
        return "fall"

def get_athlete():
    return random.choice([
        "Lebron James",
        "Michael Jordan",
        "Steph Curry",
        "Jalen Hurts",
        "Kevin Durant",
        "The Shah",
        "Bruce Jenner"
        ])

def get_enemy():
    return random.choice([
        "Vig",
        "Nikhil"
        ])

def get_weekday_response(weekday):
    if weekday == "monday":
        return random.choice([
            "starting the week strong and going to the gym",
            "birds chirping, sweating hard and working out"
            ])
    if weekday == "tuesday":
        return random.choice([
            "waking up enjoying life, smell the flowers",
            f"Call out {get_enemy()} for being foul"

            ])
    if weekday == "wednesday":
        return random.choice([
            f"can't let {get_enemy()} win. It's hump day",
            "hump day, half way through the battle!",
            f"What do you think {get_athlete()} would do if he woke up in your shoes?"
            ])
    if weekday == "thursday":
        return random.choice([
            f"aspiration achieving our dreams." ,
            "ONE MORE DAY!",
            f"Another nightmare about the ayatollah."
            ])
    if weekday == "friday":
        return random.choice([
            "telling close friends good job this week.",
            "This is it! Grand finale!"
            ])
    if weekday == "saturday":
        return random.choice([
            f"fake friendliness towards {get_enemy()}",
            "Saturday. Men are made."
            ])
    if weekday == "sunday":
        return random.choice([
            f"rest up big guys, it's about to repeat."
            ])

def determine_prompt(holiday= None, day= None, week= None):
    if day == None:
        day = now.isoweekday()
    if holiday == None:
        holiday = us_holidays.get(today_str)
    if week == None:
        week = now.isocalendar().week
    season = week_enu(week)
    day = day_enu[day]
    #print(f"Holiday: {holiday}, Day: {day}, Season: {season}")
    if holiday == "New Year's Day":
        return f"Happy new years message"
    if holiday == "Martin Luther King Jr. Day":
        return f"gratitude for Martin Luther King Jr."
    if holiday == "Memorial Day":
        return f"Excitement for the start of summer, memorial day"
    if holiday == "Independence Day":
        return f"disdain for british colonizers. Love America!"
    if holiday == "Labor Day":
        return f"Praiseful retrospect about how hard everyone works"
    if holiday == "Columbus Day":
        return f"Hateful statement about christopher columbus"
    if holiday == "Veterans Day":
        return f"Admiration for veterans, go off on tangent about the how great the shah of iran was"
    if holiday == "Christmas Day":
        return f"enjoyment of christmas and love for the shah"
    
    pr = get_weekday_response(day)
    print(pr) 
    return pr


if __name__ == "__main__":
    for j in range(5):
        for i in range (1,8):
            print(talk(determine_prompt(day = i)))
            time.sleep(6.5)

    exit()
    for ptr in holidays.US(years = int(today_str.split('-')[2])).items():
        pr = determine_prompt(ptr[1])
        if pr != None:
            time.sleep(1.85)
            print(talk(pr))
