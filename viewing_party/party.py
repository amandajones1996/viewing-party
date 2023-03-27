# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if  title and genre and rating: 
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating 
        }
        return new_movie
    return None


def add_to_watched(user_data, movie): 
    if movie.items():
        user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    if movie:
        user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title): 
    # if title not in user_data["watchlist"]:
    #     return user_data
    for value in user_data.values():
        for movie in value: 
            if movie["title"] == title: 
                user_data["watchlist"].remove(movie)
                user_data["watched"].append(movie)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data): 
    sum = 0
    rating_average = 0
    for watched in user_data["watched"]: 
        sum += watched["rating"]
        rating_average = sum / len(user_data["watched"])
    return rating_average




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

