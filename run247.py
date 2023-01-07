
from fb_new import send_mess_to_chat
import random
import datetime
import time
import os
os.system("xset dpms force off")
# using now() to get current time


active_hours={
    (1,2):"night",
    (3,4):"undefined",
    (5,9):"morning",
    (10,16):"undefined",
    (17,24):"night"
    }

max_messages={
    "morning":1,
    "night":2,
    "not-defined":0
}

current_day=datetime.datetime.now().day
current_period="not-defined"
current_period_hours=None
messages_in_current_period=0

while True:
    ct = datetime.datetime.now()
    print(f"\n{ct.day}/{ct.hour}:{ct.minute}:{ct.second}")
    if ct.day != current_day:
        current_day = ct.day
        for key in max_messages:
            max_messages[key]=0 #reset the count for the day to 0   

    print(current_period)
    for period in active_hours:
        if ct.hour >= period[0] and ct.hour <= period[1]:
            if current_period != active_hours[period]:
                print("period has changed")
                current_period=active_hours[period]
                period_set= True
                messages_in_current_period=0 #reset current messages in period to 0 because period changed.
            current_period_hours=period

    time.sleep(5)
    print(f"current period: {current_period}")
    if current_period != "not-defined":
        prob_range=((current_period_hours[1]-current_period_hours[0])*60)/max_messages[current_period]
        
        print(f"Probability: {prob_range}. Messages in current period: {messages_in_current_period}. Max messages allowed: {max_messages[current_period]} ")
        
        chosen_number= random.choice(range(int(prob_range)))
        print(f"{chosen_number} chosen out of {prob_range}, will send message if 1 is selected.")
        if chosen_number == 1:
            if messages_in_current_period < max_messages[current_period]:
                print("Sending message to chat")
                messages_in_current_period+=1
                send_mess_to_chat()
                os.system("xset dpms force off")

            else:
                print("Max messages for this time period already sent.")
    
            
        