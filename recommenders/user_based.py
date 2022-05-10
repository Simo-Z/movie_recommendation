import pandas as pd
def top_n_movies_user_based(user_id, n_movies: int = 5):
    path = "./cleaned_data/"
    ratings = pd.read_csv(f"{path}cl_ratings.csv")
    sparse_matrix = ratings.pivot(index='movieId', columns='userId', values='rating')
    
    movies_df = (
    sparse_matrix
        .corrwith(sparse_matrix[user_id])
        .sort_values(ascending=False)
        .head(n_movies + 1)
        .reset_index()
        .iloc[1:]
    )
    return movies_df