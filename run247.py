
from fb_new import send_mess_to_chat
import random
import datetime
import time
import os
#os.system("xset dpms force off")
# using now() to get current time


active_hours_messages={
    (1,2):1,
    (16,23):2,
    (3,7):1
    }



current_day=datetime.datetime.now().day - 1
print(current_day)


message_times = []
while True:
        
    time.sleep(.25)
    ct = datetime.datetime.now()
    if ct.day != current_day:
        current_day=ct.day
        for times in active_hours_messages:
            for i in range(active_hours_messages[times]):
                slotting = True
                while slotting:
                    hour = random.randrange(times[0],times[1]+1)
                    minutes = random.randrange(1,60)
                    if hour not in [int(event.split("/")[0]) for event in message_times]:
                        message_times.append(f"{hour}/{minutes}")
                        slotting=False


    for message_event in message_times:
        if f"{ct.hour}/{ct.minute}" == message_event:
            print("sending message")
            
            send_mess_to_chat()
            message_times.remove(message_event)
        else: print(f"{ct.hour}/{ct.minute} != {message_event}")
            
    print(f"currently scheduled events: {message_times}")
    print(f"\n{ct.day}/{ct.hour}:{ct.minute}:{ct.second}")
    os.system("xset dpms force off")

    
            
        