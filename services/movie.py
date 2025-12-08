from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None) -> list | None:
    movie = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return movie

    if genres_ids:
        movie = movie.filter(genres__id__in=genres_ids)
    if actors_ids:
        movie = movie.filter(actors__id__in=actors_ids)
    return movie


def __str__(self) -> str:
    return self.name


def get_movie_by_id(movie_id: int) -> dict | None:
    if not movie_id:
        return None
    if movie_id:
        return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None,
) -> dict | None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
