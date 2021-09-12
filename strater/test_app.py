
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import APP
from models import setup_db

producer_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTE1NzViOGUzMWQ1MDA2OWY4NzRlYSIsImF1ZCI6ImZwIiwiaWF0IjoxNjMxNDY4NTYyLCJleHAiOjE2MzE1NTQ5NjIsImF6cCI6InRMRUVpOEpIelhXWEhxVEJiN1F4V3FRbDNDTHBISGVHIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.J9fg2a6Ib28VZW1tKqOPnxIBpakra-9EJDA-taCXKblCHQWn_QKBXpoLuk3geYx96Ey2b-nBfiU6lwJ7XqayreaWdeaRv5L-bvCPxAJq2IiZRYMrczq1CVC-2LMJBgGOjXWDgUPscLa-J9CftE6Jk8z_KMt7Vq8_jptxVlayom3Fpc3lyvGfsmMHyDydz_2BrD3En0D0pjP27dBFX_XzH4YYO-IKyufJCDqIZfW2zbf6QlrIUXzBR3jqDLXUdKs3RMmlXA1upTu5AyzJNpBKxWlWgWEDAVfTtHu7khuoqFD7dj-M4R4U-8JV7RhO7sLU-HNC844-w7geF6CpFK8UUw'
assistance_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTE4MmY4YzcyNDA1MDA3MWI4MmE0NSIsImF1ZCI6ImZwIiwiaWF0IjoxNjMxNDY4Njk1LCJleHAiOjE2MzE1NTUwOTUsImF6cCI6InRMRUVpOEpIelhXWEhxVEJiN1F4V3FRbDNDTHBISGVHIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.V6vwFEiGFR0Ag0hHNoaDIvKJxB05BfkSwq442lUmMPpyWk5xisW5jhbhWriMia87x_14wkJE1DCqTEbv4VeLwUa90gXnQ56KYVQ6K62Cq-RukXj5yX-7tyxpovuLgD_aFScSaYu3cbXaw6px5eADPWANE5Pen4EGe8OX_7TGlC4Z27HJcaahGlatH4WeOaz-DSBdopgmV1PI2CHRjyxkCc5s-rSM-6FqFEseGvfUzejpidPD3wtiKUzekLeL0chJbo5ywuOnpZUZbB6ns30w982RmjirUhEfdXhztusmLxz3nTnBSNzmF7SIsRrCA0YT4Ssb55A306sYGsNWzGPPxw'
director_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmYwMzc4MTlmODBmMDA2OWQ0NjY0NyIsImF1ZCI6ImZwIiwiaWF0IjoxNjMxNDY5NzYwLCJleHAiOjE2MzE1NTYxNjAsImF6cCI6InRMRUVpOEpIelhXWEhxVEJiN1F4V3FRbDNDTHBISGVHIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiXX0.E3ADJZXqT9Q2eLMfv6b0wwQlz_SSIJ5qkB_vXWF7XNZUoC8Kcd1XydzXe1FPSKFPQJKReMhtdot3auvefgjVZBnIB7m1_0rS7soutDaiIgp9rJzFKQSOm8UU1KXhGh7YL6-IFJj8NyrQ636mUryXX3ksN6I34Qy_OOBLI9Sd5-HW4q1J4n2U0XI7GP3PySGN9psJncg8iy8UvqOkfyTpbGLEq74zxN3bSg4M-RACQ-YWivN5AQFDQXShFkD9_VW5uwh4X1gtgctAJmMwaT30JE65RwztZKEenYOEZ82UYeqayJ7tGPRgk-CyRB15uaFvZ1O6xCT67kbidoU5yzKj2w'

class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP
        self.client = self.app.test_client
        self.database_name = "finalproject_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres','123321','localhost:5432',self.database_name)
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
        res = self.client().get('/movies', headers=assistance_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_movies(self):
        res = self.client().get('/actors', headers=assistance_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_create_new_movie(self):
        request = {
            'title': 'inception',
            'release_date': '2010-07-10'
        }

        res = self.client().post('/add-movie', json=request, headers=director_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_create_new_actor(self):
        request = {
            'name': 'The rock',
            'age': '49',
            'gender': 'male'
        }

        res = self.client().post('/add-actor', json=request, headers=director_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_422_create_new_movie(self):
        request = {
            'title': 'maze runner',
            'release_date': ''
        }

        res = self.client().post('/add-movie', json=request, headers=director_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)


    def test_422_create_new_actor(self):
        request = {
            'name': 'Selena Gomez',
            'age': '',
            'gender': 'female'
        }

        res = self.client().post('/add-actor', json=request, headers=director_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  
    def test_update_movie(self):
      
        request = {
            'title': 'ush',
            'release_date': '2000-3-29'
        }
        
        res = self.client().patch('/movies/1', json=request, headers=producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])


    def test_update_actor(self):
      
        request = {
            'age': '28'
        }
        
        res = self.client().patch('/movies/1', json=request, headers=producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_422_update_movie(self):

        request = {
            'title': ''
        }
        res = self.client().patch('/movies/1', json=request, headers=producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])


    def test_422_update_actor(self):

        res = self.client().patch('/movies/1000', json='', headers=producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])


    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
   
    def test_delete_movie(self):
        res = self.client().delete('/movies/2', headers=producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)


    def test_delete_actor(self):
        res = self.client().delete('/actors/2', headers=producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_404_delete_movie(self):
        res = self.client().delete('/movies/0', headers=producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    def test_404_delete_actor(self):
        res = self.client().delete('/actors/0', headers=producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        

if __name__ == "__main__":
    unittest.main()
