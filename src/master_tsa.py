import re
import json
import time
from datetime import datetime,timedelta
from collections import Counter
import time
from config import get_spider_config,get_start2end_time
_,db,r = get_spider_config()

tweet_epoch = 1288834974657
def get_task():
    from_date , to_date = get_start2end_time()
    start_time = datetime.strptime(from_date,"%Y-%m-%d %H:%M:%S")
    end_time   = datetime.strptime(to_date,"%Y-%m-%d %H:%M:%S")-timedelta(seconds=1)
    for i in range(7800):
        timestamp_max = int(time.mktime((end_time-timedelta(seconds=i)).timetuple())*1000)
        timestamp_min = int(time.mktime((end_time-timedelta(seconds=i+1)).timetuple())*1000)
        max_position = (timestamp_max-tweet_epoch)<<22
        min_position = (timestamp_min-tweet_epoch-1)<<22
        message = {
            'from_date':"2012-10-10",
            'to_date':"2012-10-11",
            'this':(end_time-timedelta(seconds=i)).strftime("%Y-%m-%d %H:%M:%S"),
            "max_position":max_position,
            "min_position":min_position
        }
        print(message)
        r.rpush("task:event",json.dumps(message))

if __name__ == '__main__':
	get_task()
