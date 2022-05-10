import pandas as pd
import streamlit as st
@st.cache
def top_n_movies_popularity_based(n_movies: int = 5):
    path = "./data/clean/"
    movies = pd.read_csv(f"{path}movies.csv")
    ratings = pd.read_csv(f"{path}ratings.csv")

    return  (
    ratings
        .groupby("movieId")
        .agg(mean_rating= ("rating", "mean"), count_rating= ("rating","count"))
        .round(1)
        .sort_values("mean_rating", ascending=False)
        .query("count_rating > 100")
        .head(n_movies)
        .reset_index()
        .merge(movies)
        .filter(["title", "image_url","genres", "mean_rating", "count_rating"])
    )