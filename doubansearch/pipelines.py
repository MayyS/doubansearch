# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from doubansearch.settings import *

class DoubansearchPipeline(object):
    def __init__(self):
        host=MONGO_HOST
        port=MONGO_PORT
        dbname=MONGO_DB_NAME
        collection=MONGO_DB_COLLECTION
        client=pymongo.MongoClient(host,port)
        mydb=client[dbname]
        self.post=mydb[collection]


    def process_item(self, item, spider):
        data=dict(item)
        self.post.insert_one(data)
