import pandas as DataFrame
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

@st.cache
def top_n_movies_user_based(user_id, movies: DataFrame, ratings: DataFrame, n_movies: int = 5):
    
    sparse_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')
    movies_df = cosine_similarity(sparse_matrix)
    return movies_df