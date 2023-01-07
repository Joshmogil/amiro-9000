
from fb_new import send_mess_to_chat
import random
import datetime
import time
import os
os.system("xset dpms force off")
# using now() to get current time


active_hours={
    (4,9):"morning",
    (17,23):"night"
    }

max_messages={
    "morning":1,
    "night":140
}

current_day=datetime.datetime.now().day
current_period=None
current_period_hours=None
messages_in_current_period=0

while True:
    ct = datetime.datetime.now()
    print(f"\n{ct.day}/{ct.hour}:{ct.minute}:{ct.second}")
    if ct.day != current_day:
        current_day = ct.day
        for key in max_messages:
            max_messages[key]=0 #reset the count for the day to 0   


    for period in active_hours:
        if ct.hour >= period[0] and ct.hour <= period[1]:
            if current_period != active_hours[period]:
                print("period has changed")
                current_period=active_hours[period]
                messages_in_current_period=0 #reset current messages in period to 0 because period changed.
            current_period_hours=period

    time.sleep(2)

    prob_range=((current_period_hours[1]-current_period_hours[0])*60)/max_messages[current_period]
    print(f"Probability for current period {current_period}: {prob_range}. Messages in current period: {messages_in_current_period}. Max messages allowed: {max_messages[current_period]} ")
    if random.choice(range(int(prob_range))) == 1:
        if messages_in_current_period < max_messages[current_period]:
            print("Sending message to chat")
            messages_in_current_period+=1
            send_mess_to_chat()
            os.system("xset dpms force off")
            exit()
        else:
            print("Max messages for this time period already sent.")
    
            
        