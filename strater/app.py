from operator import ge
import os
from sqlalchemy.sql.expression import null
from models import Actor, Movie, setup_db
from flask import Flask, app, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth.auth import AuthError, requires_auth

  # create and configure the app
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
setup_db(app)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
   'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods',
    'GET, POST, DELETE, OPTIONS')
    return response


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def get_movies(payload):

    formatted_movies= [movie.format() for movie in
    Movie.query.all()]
   
    if not formatted_movies:
      abort(404)

    return jsonify({
      'success': True,
      'movies':formatted_movies,
      'total_movies':len(formatted_movies)
        }), 200


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route('/actros', methods=['GET'])
@requires_auth('get:actors')
def get_actros(payload):

    formatted_actros= [actor.format() for actor in
    Actor.query.all()]

    if not formatted_actros:
      abort(404)
   
    return jsonify({
      'success': True,
      'actors': formatted_actros,
      'total_actors':len(formatted_actros)
        }), 200


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route('/movies/<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movie')
def delete_movie(payload, movie_id):
    try:
      movie = Movie.query.filter(
      Movie.id == movie_id).one_or_none()

      if movie is None:
        abort(404)

      movie.delete()

      return jsonify({
        'success': True,
        'deleted': movie_id,
      }), 200

    except Exception as e:    
     print(e)
     abort(404)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route('/actors/<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actor')
def delete_actor(payload, actor_id):
    try:
      actor = Actor.query.filter(
      Actor.id == actor_id).one_or_none()

      if actor is None:
        abort(404)

      actor.delete()
      
      return jsonify({
        'success': True,
        'deleted': actor_id,
      }), 200

    except Exception as e:    
     print(e)
     abort(404)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route('/add-movie', methods=['POST'])
@requires_auth('post:movie')
def Add_movie(payload):
   
   body = request.get_json()

   try: 

    if body['title'] is None \
      or body['title'] == ' ' \
        or body['release_date'] is None \
          or body['release_date'] == ' ':
      abort(422)
    
    title = body['title']
    releaseDate = body['release_date']

    new_movie = Movie(
      title=title,
      release_date=releaseDate
    )
    new_movie.insert()
      
    return jsonify({
      'success': True,
      'movie': new_movie.format()
     }), 200


   except Exception as e:    
     print(e)
     abort(422)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route('/add-actor', methods=['POST'])
@requires_auth('post:actor')
def Add_actor(payload):

   body = request.get_json()

   try: 

    if body['name'] is None \
      or body['name'] == ' ' \
        or body['age'] is None \
          or body['age'] == ' ' \
            or body['gender'] is None \
              or body['gender'] ==' ':

      abort(422)
    
    name = body['name']
    age = body['age']
    gender = body['gender']

    new_actor = Actor(
      name=name,
      age=age,
      gender=gender
    )
    new_actor.insert()
      
    return jsonify({
      'success': True,
      'actor': new_actor.format()
     }), 200

   except Exception as e:    
     print(e)
     abort(422)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route('/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def update_actor(payload, id):
    body = request.get_json()
    
    try:
       updated_actor = Movie.query.get(id)

       if 'name' not in body \
         or 'age' not in body \
           or 'gender' not in body:
         abort(422)

       updated_actor.name = body['name']
       updated_actor.age = body['age']
       updated_actor.gender = body['gender']

       updated_actor.update()

       return jsonify({
            "success": True, 
            "movies": updated_actor.format()
       }),200

    except Exception as e:    
     print(e)
     abort(404)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route('/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def update_movie(payload, id):
    body = request.get_json()
    
    try:
       updated_movie = Movie.query.get(id)

       if 'title' not in body \
         or 'release_date' not in body:
         abort(422)

       updated_movie.title = body['title']
       updated_movie.release_date = body['recipe']

       updated_movie.update()

       return jsonify({
            "success": True, 
            "movies": updated_movie.format()
       }),200

    except Exception as e:    
     print(e)
     abort(404)

 
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": 'Internal Server Error'
    }), 500


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": 'Bad Request'
    }), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": 'Unathorized'
    }), 401

@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        'success': False,
        'error': error.status_code,
        'message': error.error['description']
    }), error.status_code

if __name__ == '__main__':
    app.run()
    
    
  
