import pandas as pd
def top_n_movies_popularity_based(n_movies: int = 5):
    path = "./cleaned_data/"
    movies = pd.read_csv(f"{path}cl_movies.csv")
    ratings = pd.read_csv(f"{path}cl_ratings.csv")

    return  (
    ratings
        .groupby("movieId")
        .agg(mean_rating= ("rating", "mean"), count_rating= ("rating","count"))
        .assign(ratingtest = lambda x: x["mean_rating"] * (x["count_rating"] / 300))
        .round(1)
        .sort_values("ratingtest", ascending=False)
        .query("count_rating > 1")
        .head(n_movies)
        .reset_index()
        .merge(movies)
        .filter(["title", "movieId","genres"])
    )