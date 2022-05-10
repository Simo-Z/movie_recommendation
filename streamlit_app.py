import streamlit as st
import pandas as pd
from recommenders.popularity_based import top_n_movies_popularity_based
from recommenders.user_based import top_n_movies_user_based
from recommenders.item_based import top_n_movies_item_based
import streamlit.components.v1 as components

with open("./styles/style.css") as f:
    st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)
most_pop_n_movies = 5

most_pop_movie_list = top_n_movies_popularity_based(most_pop_n_movies)
item_based_movie_list = top_n_movies_item_based(movie_id = 1)
user_based_movie_list = top_n_movies_user_based(user_id=1)

links_urls = pd.read_csv("./cleaned_data/cl_links_urls.csv")
movies = pd.read_csv("./cleaned_data/cl_movies.csv")

links_urls["image_url"] = links_urls["image_url"].apply(lambda x: "https://www.themoviedb.org/t/p/w300_and_h450_bestv2/" + x) 

most_pop_movie_list = (
    most_pop_movie_list
        .merge(links_urls, how="left")
)
item_based_movie_list = (
    item_based_movie_list
        .merge(links_urls, how="left")
        .merge(movies, how="left")
)
user_based_movie_list = (
    user_based_movie_list
        .merge(links_urls, how="left", left_index=True, right_on="movieId")
        .merge(movies, how="left")
)

st.title("WBSFlix")
# Popularity based 
st.header(f"Most Popular - Top {most_pop_n_movies}")
st.image(most_pop_movie_list["image_url"].to_list(), width=120, caption=most_pop_movie_list["title"].to_list())

# Item based 
st.header("Item based")
st.image(item_based_movie_list["image_url"].to_list(), width=120, caption=item_based_movie_list["title"].to_list())

# User based 
st.header("User based")
st.image(user_based_movie_list["image_url"].to_list(), width=120, caption=user_based_movie_list["title"].to_list())
