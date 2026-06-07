import schedule
import time
import os

def monitor():

    os.system(

        "python monitor.py"

    )

schedule.every(1).minutes.do(

monitor

)

while True:

    schedule.run_pending()

    time.sleep(1)