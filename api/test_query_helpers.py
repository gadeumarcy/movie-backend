from database import SessionLocal
from query_helpers import *

db =  SessionLocal()

#Récuperer un film dont l'ID = 1
movie = get_movie(db,movie_id=1)
print(movie.title,movie.genres)
#Récupérer les cinq premiers films
movies = get_movies(db,limit=5)
for film in movies:
    print(f"ID : {film.movieId},Titre :{film.title},Genres:  {film.genres}")

#récupérer les ratings d'un fim en donnant l'ID du film et l'ID de l'utilisateur qui a noté
rating = get_rating(db,movie_id=1,user_id=5)
print(f"User ID: {rating.userId},movie ID : {rating.movieId},Rating: {rating.rating}, timeStamp : {rating.timestamp}")

#Donner la liste des films qui ont une note minimale de 3.5
ratings = get_ratings(db,min_rating = 3.5,limit = 10)
for film in ratings:
    print(f"ID : {film.movieId},Note :{film.rating}")
    
#Donner la liste des films qui ont une note minimale de 3.5 pour l'utilisateur 1
ratings = get_ratings(db,min_rating = 3.5,limit = 10,user_id=1)
for film in ratings:
    print(f"ID : {film.movieId},Note :{film.rating}")

#récuperer les tag
tag = get_tag(db,user_id=2,movie_id=60756,tag_text="funny")
print(f"User ID : {tag.userId}, Movie ID : {tag.movieId}, Tag : {tag.tag}, Timestamp : {tag.timestamp}")

#Retourner le nombre de films
n_movies =  get_movie_count(db)
print(f"Nombre de films:{n_movies}")

#Retourner le nombre d'evaluations
n_eval =  get_rating_count(db)
print(f"Nombre de films:{n_movies}")

db.close()