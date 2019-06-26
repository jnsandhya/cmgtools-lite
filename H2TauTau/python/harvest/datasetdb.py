import pymongo
import urllib
import sys 

class DatasetDB(object): 

    def __init__(self, mode='reader', db='datasets_unittests'):
        '''init connection with database.
        mode = reader(default) or writer 
        db = dataset name (datasets_unittests by default)
        will ask for user password
        '''
        if mode not in ['reader', 'writer']: 
            raise( ValueError('mode must be either "reader" or "writer"') )
        pwd = raw_input('{} password:'.format(mode))
        self.client = pymongo.MongoClient(
            'mongodb://{}:{}@localhost/?authSource={}&authMechanism=MONGODB-CR'.format(
                mode, pwd, db
                ),
            27017
            )
        self.db = self.client[db]
        
    def insert(self, coll, info):
        '''insert or update a dataset info'''
        self.db[coll].update({'name':info['name']}, 
                             info, 
                             upsert=True)

    def remove(self, coll, query): 
        '''remove entries matching query in collection coll'''
        self.db[coll].remove(query)

    def find(self, coll, query=None):
        '''find entries matching query in collection coll'''
        if query is None: 
            query = {}
        return self.db[coll].find(query)

    def count(self, coll, query=None): 
        '''count entries matching query in collection coll'''
        if query is None: 
            query = {}
        return self.db[coll].count(query)
