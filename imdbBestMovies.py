
import pip

def install(package):
	if hasattr(pip, 'main'):
		pip.main(['install', package])
	else:
		pip._internal.main(['install', package])


		if __name__ == 'teste': install('git+https://github.com/alberanid/imdbpy')


import imdb

ia = imdb.IMDb()
top250 = ia.get_top250_movies()
film = []
i = 0
while i < 50:
	for movie_count in range(0, 50):
	    # First, retrieve the movie object using its ID
	    movie = ia.get_movie(top250[movie_count].movieID)	
	    # Print movie title and genres
	    #print(movie['title'])
	    film.append(movie['title'])
	    i += 1


import json
with open('data.json', 'w') as outfile:
   	json.dump(film, outfile)	
