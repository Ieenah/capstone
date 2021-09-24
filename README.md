# Casting Agency:
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies

## Motivation:
Casting Agency is the last project of Full Stack nano-degree program by Udacity

## Dependencies:
#### Python 3.9

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Enviornment

Recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

## Roles and Permissions:
### Roles
- There are three Roles in this API:
    - casting Assistant
      - Can view all actors and all movies

    - Casting Director
        - All permissions a Casting Assistant has and…
        - Add or delete an actor from the database
        - Modify actors or movies

    - Executive Producer
        - All permissions a Casting Director has and…
        - Add or delete a movie from the database


you can find each token for each role in the setup.sh file

## Endpoins:

`GET '/actors'`
`GET '/movies'`
`POST '/add-actor'`
`POST '/add-movie'`
`PATCH '/actors/<int:actor_id>'`
`PATCH '/movies/<int:movie_id>'`
`DELETE '/actors/<int:actor_id>'`
`DELETE '/movies/<int:movie_id>'`

GET '/actors'
- Fetches a JSON object with a list of actors in the database.
- Request Arguments: None
- Returns: An object with a single key, actors, that contains multiple objects with a series of string key pairs.
```bash
curl --location --request GET 'https://leenah1.herokuapp.com/actors' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTE1NzViOGUzMWQ1MDA2OWY4NzRlYSIsImF1ZCI6ImZwIiwiaWF0IjoxNjMyNDAyMjg2LCJleHAiOjE2MzI0ODg2ODYsImF6cCI6InRMRUVpOEpIelhXWEhxVEJiN1F4V3FRbDNDTHBISGVHIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.mPPaCGCOBJrKPwoIKuSZRuBzBnoDEZVg_rawR_HFN1E6RQx1ZSM8BDB6V1rob4YVg-WX65Tk7ovyzOnwgUW0uC74q7fBkCRKI2zaOUhWlT35k5_S2tf--jfPeJjs5jzoo0B1tlw6mXBZVvQI0iRVytc1XfG_jWmPIikjGW_lturVqjiO7iBwtF0leax1eRZuT1bdFSqWmb3EAFTEqCluaL-B3c_YeX7tyTZqrt8iAnkcpYxT3mZgIE3yXAheMNg0w5mDroF2_hHTdQIuEoXJ7l67O69jt-PeQ7gpqbKDPzFuzS3AYC5UpVbionryg1-FyqVT1e6VNfh69IItyq-xXg'
```
```bash
{
   "actors":[
   {
       "gender":
            "female","id":1,"name":"Leenah","release":"21"},{"gender":"female","id":5,"name":"Leenah","release":"21"
            },        
   {
       "gender":
            "male","id":6,"name":"The rock","release":"49"},{"gender":"female","id":7,"name":"Selena Gomez","release":"29"
            },
   {
       "gender":
            "female","id":8,"name":"Marget Robbie","release":"31"}],"success":true,"total_actors":8
            }
```


GET '/movies'
- Fetches a JSON object with a list of movies in the database.
- Request Arguments: None
- Returns: An object with a single key, movies, that contains multiple objects with a series of string key pairs.
```bash 
curl --location --request GET 'https://leenah1.herokuapp.com/movies' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTE1NzViOGUzMWQ1MDA2OWY4NzRlYSIsImF1ZCI6ImZwIiwiaWF0IjoxNjMyNDAyMjg2LCJleHAiOjE2MzI0ODg2ODYsImF6cCI6InRMRUVpOEpIelhXWEhxVEJiN1F4V3FRbDNDTHBISGVHIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.mPPaCGCOBJrKPwoIKuSZRuBzBnoDEZVg_rawR_HFN1E6RQx1ZSM8BDB6V1rob4YVg-WX65Tk7ovyzOnwgUW0uC74q7fBkCRKI2zaOUhWlT35k5_S2tf--jfPeJjs5jzoo0B1tlw6mXBZVvQI0iRVytc1XfG_jWmPIikjGW_lturVqjiO7iBwtF0leax1eRZuT1bdFSqWmb3EAFTEqCluaL-B3c_YeX7tyTZqrt8iAnkcpYxT3mZgIE3yXAheMNg0w5mDroF2_hHTdQIuEoXJ7l67O69jt-PeQ7gpqbKDPzFuzS3AYC5UpVbionryg1-FyqVT1e6VNfh69IItyq-xXg'
```
```bash
{
   "movies":[
         {
           "id":1,"release":"Wed, 29 Mar 2000 00:00:00 GMT","title":"Leenah movie"
         },
         {
           "id":3,"release":"Wed, 29 Mar 2000 00:00:00 GMT","title":"titanc"
         },
         {
           "id":5,"release":"Sat, 29 Mar 2008 00:00:00 GMT","title":"inseption"
         },
         {
           "id":6,"release":"Thu, 29 Mar 2012 00:00:00 GMT","title":"the maze runner"
         },
         {
           "id":7,"release":"Fri, 29 Mar 2019 00:00:00 GMT","title":"ush"
         }
            ],
           "success":true,"total_movies":5
}
```

POST '/add-actor'
- Posts a new actor to the database, including the name, age, gender, and actor ID, which is automatically assigned upon insertion.
- Request Arguments: Requires three string arguments: name, age, gender.
- Returns: An actor object with the age, gender, actor ID, and name, status code.
```bash 
curl --location --request POST 'https://leenah1.herokuapp.com/add-actor' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTE1NzViOGUzMWQ1MDA2OWY4NzRlYSIsImF1ZCI6ImZwIiwiaWF0IjoxNjMyNDAyMjg2LCJleHAiOjE2MzI0ODg2ODYsImF6cCI6InRMRUVpOEpIelhXWEhxVEJiN1F4V3FRbDNDTHBISGVHIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.mPPaCGCOBJrKPwoIKuSZRuBzBnoDEZVg_rawR_HFN1E6RQx1ZSM8BDB6V1rob4YVg-WX65Tk7ovyzOnwgUW0uC74q7fBkCRKI2zaOUhWlT35k5_S2tf--jfPeJjs5jzoo0B1tlw6mXBZVvQI0iRVytc1XfG_jWmPIikjGW_lturVqjiO7iBwtF0leax1eRZuT1bdFSqWmb3EAFTEqCluaL-B3c_YeX7tyTZqrt8iAnkcpYxT3mZgIE3yXAheMNg0w5mDroF2_hHTdQIuEoXJ7l67O69jt-PeQ7gpqbKDPzFuzS3AYC5UpVbionryg1-FyqVT1e6VNfh69IItyq-xXg' --header 'Content-Type: application/json' --data-raw '{"name": "Marget Robbie", "age": "31","gender": "female"}'
```
```bash
{ 
  "actor":
    {
       "gender":
          "female","id":8,"name":"Marget Robbie","release":"31"
     },
          "success":true
}
```

POST '/add-movie'
- Posts a new movie to the database, including the title, release, and movie ID, which is automatically assigned upon insertion.
- Request Arguments: Requires two string arguments: title, release.
- Returns: A movie object with the movie ID, release, and title, status code .
```bash 
curl --location --request POST 'https://leenah1.herokuapp.com/add-movie' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTE1NzViOGUzMWQ1MDA2OWY4NzRlYSIsImF1ZCI6ImZwIiwiaWF0IjoxNjMyNDAyMjg2LCJleHAiOjE2MzI0ODg2ODYsImF6cCI6InRMRUVpOEpIelhXWEhxVEJiN1F4V3FRbDNDTHBISGVHIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.mPPaCGCOBJrKPwoIKuSZRuBzBnoDEZVg_rawR_HFN1E6RQx1ZSM8BDB6V1rob4YVg-WX65Tk7ovyzOnwgUW0uC74q7fBkCRKI2zaOUhWlT35k5_S2tf--jfPeJjs5jzoo0B1tlw6mXBZVvQI0iRVytc1XfG_jWmPIikjGW_lturVqjiO7iBwtF0leax1eRZuT1bdFSqWmb3EAFTEqCluaL-B3c_YeX7tyTZqrt8iAnkcpYxT3mZgIE3yXAheMNg0w5mDroF2_hHTdQIuEoXJ7l67O69jt-PeQ7gpqbKDPzFuzS3AYC5UpVbionryg1-FyqVT1e6VNfh69IItyq-xXg' --header 'Content-Type: application/json' --data-raw '{"title":"titanc", "release_date":"2000-3-29"}'
```
```bash
{
   "movie":
      {
         "id":3,"release":"Wed, 29 Mar 2000 00:00:00 GMT","title":"titanc"
       },
         "success":true
}
```

PATCH '/actors/<int:actor_id>'
- Patches an existing actor in the database.
- Request arguments: Actor ID, included as a parameter following a forward slash (/), and the key to be updated passed into the body as a JSON object. For example, to update the name and gender and age for '/actors/1'
```bash 
curl --location --request PATCH 'https://leenah1.herokuapp.com/actors/1' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTE1NzViOGUzMWQ1MDA2OWY4NzRlYSIsImF1ZCI6ImZwIiwiaWF0IjoxNjMyNDAyMjg2LCJleHAiOjE2MzI0ODg2ODYsImF6cCI6InRMRUVpOEpIelhXWEhxVEJiN1F4V3FRbDNDTHBISGVHIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.mPPaCGCOBJrKPwoIKuSZRuBzBnoDEZVg_rawR_HFN1E6RQx1ZSM8BDB6V1rob4YVg-WX65Tk7ovyzOnwgUW0uC74q7fBkCRKI2zaOUhWlT35k5_S2tf--jfPeJjs5jzoo0B1tlw6mXBZVvQI0iRVytc1XfG_jWmPIikjGW_lturVqjiO7iBwtF0leax1eRZuT1bdFSqWmb3EAFTEqCluaL-B3c_YeX7tyTZqrt8iAnkcpYxT3mZgIE3yXAheMNg0w5mDroF2_hHTdQIuEoXJ7l67O69jt-PeQ7gpqbKDPzFuzS3AYC5UpVbionryg1-FyqVT1e6VNfh69IItyq-xXg' --header 'Content-Type: application/json' --data-raw '{"name":"Nelu", "gender": "female", "age": "21"}'
```
```bash
{
   "actors":
         {
             "gender":"female","id":1,"name":"Nelu","release":"21"
          },
             "success":true 
}
```

PATCH '/movies/<int:movie_id>'
- Patches an existing movie in the database.
- Request arguments: Movie ID, included as a parameter following a forward slash (/), and the key to be updated, passed into the body as a JSON object. For example, to update the title and release date for '/movies/1'
```bash
curl --location --request PATCH 'https://leenah1.herokuapp.com/movies/1' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTE1NzViOGUzMWQ1MDA2OWY4NzRlYSIsImF1ZCI6ImZwIiwiaWF0IjoxNjMyNDAyMjg2LCJleHAiOjE2MzI0ODg2ODYsImF6cCI6InRMRUVpOEpIelhXWEhxVEJiN1F4V3FRbDNDTHBISGVHIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.mPPaCGCOBJrKPwoIKuSZRuBzBnoDEZVg_rawR_HFN1E6RQx1ZSM8BDB6V1rob4YVg-WX65Tk7ovyzOnwgUW0uC74q7fBkCRKI2zaOUhWlT35k5_S2tf--jfPeJjs5jzoo0B1tlw6mXBZVvQI0iRVytc1XfG_jWmPIikjGW_lturVqjiO7iBwtF0leax1eRZuT1bdFSqWmb3EAFTEqCluaL-B3c_YeX7tyTZqrt8iAnkcpYxT3mZgIE3yXAheMNg0w5mDroF2_hHTdQIuEoXJ7l67O69jt-PeQ7gpqbKDPzFuzS3AYC5UpVbionryg1-FyqVT1e6VNfh69IItyq-xXg' --header 'Content-Type: application/json' --data-raw '{"title":"Nelu", "release_date": "2002-12-23"}'
```
```bash
{
  "success":true
}
```


DELETE '/actors/<int:actor_id>'
- Deletes an actor in the database via the DELETE method and using the actor id.
- Request argument: Actor id, included as a parameter following a forward slash (/).
- Returns: ID for the deleted question and status code of the request.
```bash 
 curl --location --request DELETE 'https://leenah1.herokuapp.com/actors/1' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTE1NzViOGUzMWQ1MDA2OWY4NzRlYSIsImF1ZCI6ImZwIiwiaWF0IjoxNjMyNDAyMjg2LCJleHAiOjE2MzI0ODg2ODYsImF6cCI6InRMRUVpOEpIelhXWEhxVEJiN1F4V3FRbDNDTHBISGVHIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.mPPaCGCOBJrKPwoIKuSZRuBzBnoDEZVg_rawR_HFN1E6RQx1ZSM8BDB6V1rob4YVg-WX65Tk7ovyzOnwgUW0uC74q7fBkCRKI2zaOUhWlT35k5_S2tf--jfPeJjs5jzoo0B1tlw6mXBZVvQI0iRVytc1XfG_jWmPIikjGW_lturVqjiO7iBwtF0leax1eRZuT1bdFSqWmb3EAFTEqCluaL-B3c_YeX7tyTZqrt8iAnkcpYxT3mZgIE3yXAheMNg0w5mDroF2_hHTdQIuEoXJ7l67O69jt-PeQ7gpqbKDPzFuzS3AYC5UpVbionryg1-FyqVT1e6VNfh69IItyq-xXg'
 ```
 ```bash
{
   "deleted":1,
   "success":true
}
```

DELETE '/movies/<int:movie_id>'
- Deletes a movie in the database via the DELETE method and using the movie id.
- Request argument: Movie id, included as a parameter following a forward slash (/).
- Returns: ID for the deleted question and status code of the request.
```bash 
curl --location --request DELETE 'https://leenah1.herokuapp.com/movies/5' --header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImZQNk0yUUJaQjViZklxUU8tQjZoLSJ9.eyJpc3MiOiJodHRwczovL2lsZWVuYWgudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMTE1NzViOGUzMWQ1MDA2OWY4NzRlYSIsImF1ZCI6ImZwIiwiaWF0IjoxNjMyNDAyMjg2LCJleHAiOjE2MzI0ODg2ODYsImF6cCI6InRMRUVpOEpIelhXWEhxVEJiN1F4V3FRbDNDTHBISGVHIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.mPPaCGCOBJrKPwoIKuSZRuBzBnoDEZVg_rawR_HFN1E6RQx1ZSM8BDB6V1rob4YVg-WX65Tk7ovyzOnwgUW0uC74q7fBkCRKI2zaOUhWlT35k5_S2tf--jfPeJjs5jzoo0B1tlw6mXBZVvQI0iRVytc1XfG_jWmPIikjGW_lturVqjiO7iBwtF0leax1eRZuT1bdFSqWmb3EAFTEqCluaL-B3c_YeX7tyTZqrt8iAnkcpYxT3mZgIE3yXAheMNg0w5mDroF2_hHTdQIuEoXJ7l67O69jt-PeQ7gpqbKDPzFuzS3AYC5UpVbionryg1-FyqVT1e6VNfh69IItyq-xXg'
```
```bash
{
   "deleted":5,
   "success":true
}
```

## Running tests:
To run the tests, run:

- dropdb finalproject_test
- createdb finalproject_test
- python test_app.py

## Hosting

The application is hosted by heroku under the url: ['heroku app'](https://leenah1.herokuapp.com/)
