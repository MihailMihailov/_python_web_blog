import pymongo


class Database(object):
    """Database class"""
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None

    @staticmethod
    def initialize():
        """Initialize database"""
        # implement init class for different servers
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        """Save to database"""
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        """Find all queries in given collection"""
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        """Find single query in collection"""
        return Database.DATABASE[collection].find_one(query)
