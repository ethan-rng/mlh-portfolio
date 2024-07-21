import unittest
from peewee import *
from playhouse.shortcuts import model_to_dict


from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables (MODELS)
    def tearDown(self):
        test_db.drop_tables (MODELS)
        # Close connection to db.
        test_db.close()
    def test_timeline_post(self):
        # Create 2 timeline posts.
        first_post = TimelinePost.create(name='John Doe',
                                          email='john@example.com', 
                                          content='Hello world, I\'m John!',
                                          password="password1")
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe',
                                          email='jame@example.com',
                                          content='Hello world, I\'m Jane!',
                                          password="password2")
        assert second_post.id == 2
        # TODO: Get timeline posts and assert that they are correct

        fetched_posts = [model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at)]
        
        found1 = False
        found2 = False
        for post in fetched_posts:
            if post["id"] == 1:
                assert post["name"] == "John Doe" and post["email"] == "john@example.com" and post["content"] == "Hello world, I\'m John!" and post["password"] == "password1"
            if post["id"] == 2:
                assert post["name"] == "Jane Doe" and post["email"] == "jame@example.com" and post["content"] == "Hello world, I\'m Jane!" and post["password"] == "password2"
        assert not found1 
        assert not found2