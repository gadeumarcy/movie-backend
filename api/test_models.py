from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

#Tester la récupération de quelques films
movies = db.query(Movie).limit(10).all()

for movie in movies:
    print(movie.movieId,movie.title,movie.genres)
else:
    print("No movies found")
    

#Récupérer tous les films du genre Action
action_movies = db.query(Movie).filter(Movie.genres.contains("Action")).limit(5).all()

for movie in action_movies:
    print(movie.movieId,movie.title,movie.genres)
else:
    print("No action movies found")
#Tester la récupération de quelques évaluations (ratings)
Ratings  = db.query(Rating).limit(5).all()
for rating in Ratings:
    print(f"User ID: {rating.movieId},movie ID : {rating.movieId},Rating: {rating.rating}, timeStamp : {rating.timestamp}")
    
high_rated_movies=  db.query(Movie.title,Rating.rating).join(Rating).filter(Rating.rating >=4).limit(5).all()
print(high_rated_movies)
for title,rating in high_rated_movies:
    print(title,rating)
    
high_rated_movies=  db.query(Movie.title,Rating.rating).join(Rating).filter(Rating.rating >=4,Movie.movieId == Rating.movieId).limit(5).all()
print(high_rated_movies)
for title,rating in high_rated_movies:
    print(title,rating)
    
#Récupérer des tags associés aux films
tags = db.query(Tag).limit(5).all()

for tag in tags:  
    print(f"User ID : {tag.userId}, Movie ID : {tag.movieId}, Tag : {tag.tag}, Timestamp : {tag.timestamp}")


links = db.query(Link).limit(5).all()

for link in links:
    print(f"Movie ID : {link.movieId}, IMDB ID : {link.imdbId}, TMDB ID : {link.tmdbId}")

#Fermer la seesion
db.close()

