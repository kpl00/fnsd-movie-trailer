import media
import fresh_tomatoes

# Create movie objects
interstellar = media.Movie("drama", "Interstellar", "2014",
                           "Christopher Nolan",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg")  # NOQA

cloud_atlas = media.Movie("Science Fiction", "Cloud Atlas", "2012",
                          "Wachowski Brothers",
                          "https://www.youtube.com/watch?v=hWnAqFyaQ5s",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczMTgxMjc4NF5BMl5BanBnXkFtZTcwNjM5MTA2OA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg")  # NOQA

arrival = media.Movie("Science Fiction", "Arrival", "2016",
                      "Dennis Villeneuve",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g",
                      "https://lh3.googleusercontent.com/JosEdCXr36Aa1pIyVCe-_9MjY4FFOudb52MLztpIN2eA8OMlCsSB9YNGtV_x7m7APY7y0Q=w300")  # NOQA

# Combine movie objects into an array
movies = [interstellar, cloud_atlas, arrival]

# Launch movies array in fresh_tomatoes.py - a showcase webpage for the movies
fresh_tomatoes.open_movies_page(movies)
