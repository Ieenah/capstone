
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import APP
from models import setup_db

producer_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTE1NzViOGUzMWQ1MDA2OWY4NzRlYSIsImF1ZCI6ImRldiIsImlhdCI6MTYzMTI3NjE0NiwiZXhwIjoxNjMxMzYyNTQ2LCJhenAiOiJyWG9tdnRITkloa1RjeTZnaDY3elJFTG1jdmtIWTBNeCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.TE-2jpyAaIRklEOKr4nm7V863pSNS0K238VRdaCl6Jd2KDfROwjpZCtpSCsiEtuuolGOC5lEGWTQooKij4IMPMTi9lZHtNZnBzmQKV4abcSSNjk0GomUCI2TUeYCJ0UV5txgtmvSfzaxYJAK4vneYcyZzYjSpbqXqU6MUdeMGiOQjW5Z22ktMezY7M1A7HeoS9KA92MnCPGFqj-zXrgv4-gw46cZBegD82NcCU2DnmgknpgvGF_mBIAjv9Sa5Jhh_-cIUM-A5T2TfPS5X8Eeej7vBnAK6g9oj8ZuWG0GobUipqFqzLf_pi9cc9QHUV5ADHosWZDl7F5k6Doce1z6Vg'
assistance_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTE4MmY4YzcyNDA1MDA3MWI4MmE0NSIsImF1ZCI6ImRldiIsImlhdCI6MTYzMTI3NjYyMSwiZXhwIjoxNjMxMzYzMDIxLCJhenAiOiJyWG9tdnRITkloa1RjeTZnaDY3elJFTG1jdmtIWTBNeCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.pG-YzAkIYou9MlygOo05pHBLFwP03nxWg6W57WGXn7_XtEXnZPBEFzgNKqn1Xubg-sosR8tUIv_AnsEHotW5yHES5BpN4xi698w8YyPtEFVeJbr9ffKHC-PZHZ4bVpFJQ_h-3HZCvJzZj-m05InMsz42d13Rr-7hGzcG_AUhzdtcfsDsYYW7LmUf_bHyf7eKfcnLeHMzlE5ZTDN_vRtASkZwbsFa5TWLl4Bok6XncwEQm5Vd2PwXoyl44SoGRg2ihCrJRdkuBv2wxMchq5_reR73CqSRpzllrlU-bFGxHju8lzdW-vCWg_FT-dFPMjei_VoBr9wTFFnR9SjFQwxoaA'
director_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmYwMzc4MTlmODBmMDA2OWQ0NjY0NyIsImF1ZCI6ImRldiIsImlhdCI6MTYzMTI3Njc2NSwiZXhwIjoxNjMxMzYzMTY1LCJhenAiOiJyWG9tdnRITkloa1RjeTZnaDY3elJFTG1jdmtIWTBNeCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9yIl19.f45AvbrZklAZzEqClNP1L9RlEDbfeKnrT6h9pEYjXk1HkqUERLI7cCukHB3780e5yo-GfaaJonu6Fc_XkI1sA0dNdngm9NwvvStutFCsaSQvdXXqnmvqWj0wdkspQuMP8fJMQijN5-imNU6dKGPsCkwX3LH8s3ld2kFKLsPneEMuVs_0nInwFJAr0TxMaY1Zm5Smavipo3IjTYakUoNrlsG2ICDd4-bauU6FjkEpw67mJmDCu1ObW42t550uTpUYizqajoNVsNy4xYWdubw_c1FRJoqNJbN8c-MTM2F0JAS14eIi-y8qBdrXRAnXV92KAjVj50z39Rl1DyqOuIAz-A'

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
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_create_new_movie(self):
        request = {
            'title': 'inception',
            'release_date': '2010-07-10'
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
            'title': 'ush',
            'release_date': '2000-3-29'
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
        

if __name__ == "__main__":
    unittest.main()
