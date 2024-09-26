def movie_organizer(*movies):
    genre_dict = {}
    for movie, genre in movies:
        if genre in genre_dict:
            genre_dict[genre].append(movie)
        else:
            genre_dict[genre] = [movie]
    sorted_genres = sorted(genre_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for genre, movie_list in sorted_genres:
        result += f"{genre} - {len(movie_list)}\n"
        for movie in sorted(movie_list):
            result += f"* {movie}\n"
    return result
