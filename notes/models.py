from django.db import models
from django.utils.timezone import now


class User(models.Model):
	username = models.CharField(max_length=40)
	password = models.CharField(max_length = 40)
	user_id = models.IntegerField()


class Note(models.Model):
	title = models.CharField(max_length = 100)
	content = models.CharField(max_length = 5000)
	note_id = models.CharField(max_length = 10)
	date_updated = models.DateTimeField(default=now)
	user_created = models.CharField(max_length=40)






























#idea: imdb style mini app, Movie model, user, header with sign up or log in {{if session == None:}}})
#in home: /viewmovie
#in home, search bar = with/search, method = "GET"
#search a movie, bring up movie in db: cast, summary, title, overall_rating - init. to 0.0
#usereview: summary, user, content, etc.
#on backend: movie_keywords = request.get("") equivalent in django, Movie.objects.filter(movie_title.contains(movie_keywords))
#paginate, when clicked on: /viewmovie/<id>
#summary, title, overall_rating, user_reivews: 
#/userreviews/<id>, Movie.objects.filter(movie = movie, id = id) - no pagination (for easy at first)
#filter by rating: form with sort by, rating inc, rating dec, review_date, default: helpfulness, apply button
#on backend: if request.get("sort") == "": sort = "helpfullness" else: sort = request.get("sort")
#if sort == "reviewdate": models.objects.orderby(date).all()
#to add pagination: if request.get("page") == "" page = 1 else: page = request.get("page")
#models.paginate(page=page) for page in iter_pages():   <a href='127:000/userreviews/<id>/sort=sort'>{{page}}</a>

#style: colored background, movie font, fun, popcorn picture on home, curtains for each movie, large font



