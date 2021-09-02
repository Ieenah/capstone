
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from .app import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agency_test"
        self.database_path = "postgres://{}/{}".format('project2','localhost:5432',self.database_name)

        setup_db(self.app, self.database_path)        

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass 


    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_movies(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
   
    def test_delete_movie(self):
        res = self.client().delete('/movies/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)


    def test_delete_actor(self):
        res = self.client().delete('/actors/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_404_delete_movie(self):
        res = self.client().delete('/movies/0')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_404_delete_actor(self):
        res = self.client().delete('/actors/0')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_create_new_movie(self):
        request = {
            'title': 'inception',
            'release_date': '08/07/2010'
        }

        res = self.client().post('/add-movie', json=request)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_create_new_actor(self):
        request = {
            'name': 'The rock',
            'age': '49',
            'gender': 'male'
        }

        res = self.client().post('/add-actor', json=request)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_422_create_new_movie(self):
        request = {
            'title': 'maze runner',
            'release_date': ''
        }

        res = self.client().post('/add-movie', json=request)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)


    def test_422_create_new_actor(self):
        request = {
            'name': 'Selena Gomez',
            'age': '',
            'gender': 'female'
        }

        res = self.client().post('/add-actor', json=request)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  
    def test_update_movie(self):
      
        request = {
            'title': 'ush'
        }
        
        res = self.client().patch('/movies/1', json=request)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])


    def test_update_actor(self):
      
        request = {
            'age': '28'
        }
        
        res = self.client().patch('/movies/1', json=request)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_422_update_movie(self):

        request = {
            'title': ''
        }
        res = self.client().patch('/movies/1', json=request)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])


    def test_422_update_actor(self):

        request = {
            'age': ''
        }
        res = self.client().patch('/movies/1', json=request)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

if __name__ == "__main__":
    unittest.main()
