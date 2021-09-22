

import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import APP, create_app
from models import setup_db, db_drop_create_all


producer_token = os.environ.get("producer_token")
assistance_token = os.environ.get("assistance_token")
director_token = os.environ.get("director_token")


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP
        self.client = self.app.test_client
        database_name = "finalproject_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            'postgres', '123321', 'localhost:5432', database_name)

        setup_db(self.app, self.database_path)
  
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)


    def tearDown(self):
        """Executed after reach test"""
        pass


    def test_create_new_movie(self):
        request = {
            'title': 'inception',
            'release_date': '2010-07-10'
        }

        res = self.client().post('/add-movie', json=request, headers={
            "Authorization": "Bearer {}"+producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_actor(self):
        request = {
            'name': 'The rock',
            'age': '49',
            'gender': 'male'
        }

        res = self.client().post('/add-actor', json=request, headers={
            "Authorization": "Bearer {}"+producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_403_create_new_movie(self):
        request = {
            'title': 'maze runner',
            'release_date': ''
        }

        res = self.client().post('/add-movie', json=request, headers={
            "Authorization": "Bearer {}"+assistance_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)

    def test_403_create_new_actor(self):
        request = {
            'name': 'Selena Gomez',
            'age': '',
            'gender': 'female'
        }

        res = self.client().post('/add-actor', json=request, headers={
            "Authorization": "Bearer {}"+assistance_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)


    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_get_movies(self):
        res = self.client().get('/movies', headers={
            "Authorization": "Bearer {}"+assistance_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_actors(self):
        res = self.client().get('/actors', headers={
            "Authorization": "Bearer {}"+assistance_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_401_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)




    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


    def test_update_movie(self):

        request = {
            'title': 'ush',
            'release_date': '2000-3-29'
        }

        res = self.client().patch('/movies/2', json=request, headers={
            "Authorization": "Bearer {}"+producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_update_actor(self):

        request = {
            'name': 'loly', 'age': '22', 'gender' : 'female'
        }

        res = self.client().patch('/actors/2', json=request, headers={
            "Authorization": "Bearer {}"+producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])


    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


    def test_403_update_movie(self):

        request = {
            'title': 'ush',
            'release_date': '2000-3-29'
        }

        res = self.client().patch('/movies/2', json=request, headers={
            "Authorization": "Bearer {}"+assistance_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)

    def test_403_update_actor(self):

        request = {
            'name': 'loly', 'age': 22
        }
        res = self.client().patch('/actors/2', json=request, headers={
            "Authorization": "Bearer {}"+assistance_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)


    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


    def test_delete_movie(self):
        res = self.client().delete('/movies/6', headers={
            "Authorization": "Bearer {}"+producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 6)


    def test_delete_actor(self):
        res = self.client().delete('/actors/6', headers={
            "Authorization": "Bearer {}"+producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 6)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_404_delete_movie(self):
        res = self.client().delete('/movies/0', headers={
            "Authorization": "Bearer {}"+producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_404_delete_actor(self):
        res = self.client().delete('/actors/0', headers={
            "Authorization": "Bearer {}"+producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


if __name__ == "__main__":
    unittest.main()
