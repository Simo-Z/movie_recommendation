import pandas as pd
import streamlit as st
@st.cache
def top_n_movies_item_based(movie_title: int, movies: pd.DataFrame, ratings: pd.DataFrame, n_movies: int = 5):
    movie_id = movies.query("title == @movie_title")["movieId"].to_list()[0]
    sparse_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')
    movies_df = (
    sparse_matrix
        .corrwith(sparse_matrix[movie_id])
        .sort_values(ascending=False)
        .reset_index()
        .query("movieId != @movie_id")
        .head(n_movies )
        .merge(movies, how="left")
        
    )
    return movies_df

