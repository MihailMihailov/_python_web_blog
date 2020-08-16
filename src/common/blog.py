import uuid
import datetime

from src.common.database import Database
from src.common.post import Post


class Blog(object):
    """Blog class"""

    def __init__(self, author, title, description, author_id, _id=None):
        """Initialize the Blog class"""
        self.author = author
        self.title = title
        self.description = description
        self.author_id = author_id
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, date=datetime.datetime.utcnow()):
        """Get a new post and save it to the database"""
        post = Post(blog_id=self._id,
                    title=title,
                    content=content,
                    author=self.author,
                    created_date=date)

        post.save_to_mongo()

    def get_posts(self):
        """Get posts by ID"""
        return Post.from_blog(_id=self._id)

    def save_to_mongo(self):
        """Save post to database"""
        Database.insert('blogs',
                        data=self.json())

    def json(self):
        """Format of the post"""
        return {'author': self.author,
                'title': self.title,
                'description': self.description,
                'author_id': self.author_id,
                '_id': self._id}

    @classmethod
    def from_mongo(cls, _id):
        """Get all the data by ID"""
        blog_data = Database.find_one(collection='blogs',
                                      query={'_id': _id})
        return cls(**blog_data)

    @classmethod
    def find_by_author_id(cls, author_id):
        """Get blogs by author"""
        blogs = Database.find(collection='blogs',
                              query={'author_id': author_id})

        return [cls(**blog) for blog in blogs]
