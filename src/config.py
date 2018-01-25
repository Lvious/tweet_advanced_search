import pymongo
import redis

def get_spider_config():
    
    spider = "hello"
    client = pymongo.MongoClient(host='54.210.116.149',port=27017)
    db = client.tweet_lv
    r = redis.StrictRedis(host="54.161.160.206",port=6479,db=0)

    return spider,db,r

def get_collections_name():
    SPIDER = "day"
    CLUSTER = "day_cluster"
    return SPIDER,CLUSTER
