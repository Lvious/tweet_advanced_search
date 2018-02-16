#-*- coding:utf8 -*-
import datetime
import json
import time
import os
import pytz
import requests
from bs4 import BeautifulSoup as bs
import sys

from config import get_spider_config,get_collections_name
_,db,r = get_spider_config()
SPIDER,_ ,LOG = get_collections_name()


if __name__ == '__main__':
    print 'writer start!'
    count = 0
    bulk_reqs = []
    while True:
        queue = r.lpop('task:insert')
        count+=1
        # print(queue)
        if queue:
            message = json.loads(queue)
            bulk_reqs.append(InsertOne(message))
            if count %1000 == 0:
                print 'writer process!'
                db[SPIDER].bulk_write(bulk_reqs)
                bulk_reqs=[]
                print 'writer bulk!'