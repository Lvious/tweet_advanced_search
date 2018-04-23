import pymongo
import redis
import os

def get_spider_config():
    spider = "hello"
    client = pymongo.MongoClient(host=os.environ['MONGOHOST'],port=int(os.environ['MONGOPORT']))
    db = client.tweet_event
    r = redis.StrictRedis(host=os.environ['REDISHOST'],port=int(os.environ['REDISPORT']),db=0)

    return spider,db,r

def get_collections_name():
    SPIDER = "event"
    CLUSTER = "day_cluster"
    LOG = "event_log"
    return SPIDER,CLUSTER,LOG

def get_start2end_time():
	start = "2012-10-10 00:00:00"
	end = "2012-10-10 02:10:00"
	return start,end

# if __name__ == '__main__':
# 	t1 ,t2 = get_start2end_time()
# 	print(t1)
# 	print(t2)