#-*- coding:utf8 -*-
import datetime
import json
import time
import os
import pytz
import requests
from bs4 import BeautifulSoup as bs
import sys
from pymongo import InsertOne
from pymongo.errors import BulkWriteError
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
            bulk_reqs.append(message)
            if count %1000 == 0:
                print 'writer process!'
                try:
                    db[SPIDER].bulk_write([InsertOne(i) for i in bulk_reqs])
                except BulkWriteError as bwe:
                    for i in bulk_reqs:
                        r.rpush('task:insert',json.dumps(i))
                    print(bwe.details)                        
                bulk_reqs=[]
                print 'writer bulk!'
