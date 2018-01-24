import pymongo
import redis

def get_spider_config():
    db = pymongo.MongoClient(host='54.161.160.206',port=29017)
    r = redis.StrictRedis(host="101.132.114.125",port=6379,db=0)
    return _,db,r

def get_collections_name():
    SPIDER = "day"
    CLUSTER = "day_cluster"
    return SPIDER,CLUSTER