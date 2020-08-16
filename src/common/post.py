import uuid
import datetime

from src.common.database import Database


class Post(object):
    """Post class"""

    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        """Initialize"""
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        """Save to database"""
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        """Format for the post"""
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    def from_mongo(cls, _id):
        """Get post data by give id"""
        # @TODO make if for different collections
        post_data = Database.find_one(collection='posts', query={'_id': _id})
        return cls(**post_data)

    @staticmethod
    def from_blog(id):
        """Get all post by given blog ID"""
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]

    @staticmethod
    def from_mongo_by_author(author):
        """Get from database by author"""
        return [post for post in Database.find(collection='posts', query={'author': author})]
