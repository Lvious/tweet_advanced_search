import pymongo
import redis
import os
def get_spider_config():
    
    spider = "hello"
    client = pymongo.MongoClient(host=os.environ['MONGOHOST'],port=os.environ['MONGOPORT'])
    db = client.tweet_lv
    r = redis.StrictRedis(host=os.environ['REDISHOST'],port=os.environ['REDISPORT'],db=0)

    return spider,db,r

def get_collections_name():
    SPIDER = "day"
    CLUSTER = "day_cluster"
    return SPIDER,CLUSTER
