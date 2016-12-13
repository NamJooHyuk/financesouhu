#encoding: utf-8
from pymongo import MongoClient
from scrapy.conf import settings
client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
News_souhuDB = client[settings['MONGODB_DB']]
collect_souhu_161212 = News_souhuDB[settings['MONGODB_COLLECTION']]