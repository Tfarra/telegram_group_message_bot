import sys
from telethon import TelegramClient
import time
import datetime
from datetime import date
import os, os.path
import asyncio
from telethon import errors

######## API CONFIG #######

api_id=00000000 # Insert api id (int)
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxx' # Insert api hash (string)

####### SET GROUPS TO MESSAGE #######

groups = ['RavencoinDev', 
 'travala',
 'unigemchatz',
 'defiandmore',
 'dexgemschat',
 'kybernetwork1',
 'UNITED_SHILLERS',
] # Insert the group usernames as shown above. You must have previously joined them.

gset=set(groups)
groups=list(gset) # eliminate duplicates

####### END GET SHILL GROUPS #####


async def work():
        async with TelegramClient('anon',api_id,api_hash) as client:
            while(True):
                failcount=0
                
                ###### MESSAGE SETTING ######
                
                message='Im selling X and Y. Dm me if interested ;). Have a great day!'
                
                #############################
                
                for x in groups:
                    try:                     
                        await client.send_message(x,message) # SEND MESSAGE
                        print('Sent to group: ' + x)
                        time.sleep(1) # 1 SECOND SLEEP BETWEEN GROUPS
                        
                    except errors.FloodWaitError as e:
                        print('FLOODED FOR ', e.seconds)
                        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                        time.sleep(e.seconds+2)
                        failcount+=1
                    except Exception as e:
                        print("Error:", e)
                        print("Trying to continue...")
                        print(x, sys.exc_info()[0])
                        failcount+=1
                        continue

                print(datetime.datetime.now(),str(failcount/len(groups)*100)+ '%')
                time.sleep(1300)
    
####### Asyncio and loop handling #######
       
try:
    loop = asyncio.get_running_loop()
except RuntimeError:  # 'RuntimeError: There is no current event loop...'
    loop = None

if loop and loop.is_running():
    print('Async event loop already running. Adding coroutine to the event loop.')
    tsk = loop.create_task(work())
    # ^-- https://docs.python.org/3/library/asyncio-task.html#task-object
    # Optionally, a callback function can be executed when the coroutine completes
    tsk.add_done_callback(
        lambda t: print(f'Task done with result={t.result()}  << return val of main()'))
else:
    print('Starting new event loop')
    asyncio.run(work())
