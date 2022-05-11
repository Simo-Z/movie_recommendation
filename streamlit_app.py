import streamlit as st
import pandas as pd

from recommenders.popularity_based import top_n_movies_popularity_based
from recommenders.item_based import top_n_movies_item_based
from recommenders.user_based import top_n_movies_user_based


from sklearn.metrics.pairwise import cosine_similarity

# Import extra Styles
with open("./styles/style.css") as f:
    st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

# create Sidebar ----------------------------------------------
st.sidebar.title("Personalize Recommendations")
# import Data
@st.cache
def load_dfs():
    return [pd.read_csv("./data/clean/movies.csv"),pd.read_csv("./data/clean/ratings.csv")]


movies, ratings = load_dfs()
# st.dataframe(movies)
    
# Population Based Recommendations

most_pop_movies_df = top_n_movies_popularity_based()

# Item based Reccomender
fav_movie = st.sidebar.selectbox("Pick a movie you like:",  options=movies["title"])
item_based_movies_df = top_n_movies_item_based(fav_movie, movies, ratings)


# # User based Reccomender
user_id = st.sidebar.selectbox("Select a UserId:",  options=ratings["userId"].unique())
user_based_movies_df = top_n_movies_user_based(user_id, movies, ratings)



# User Interface ----------------------------------

st.title("WBSFlix")
# Popularity based 
st.header(f"Most Popular - Top 5")
st.image(most_pop_movies_df["image_url"].to_list(), width=120, caption=most_pop_movies_df["title"].to_list())

# Item based 
# st.dataframe(item_based_movies_df)
st.markdown(f"<h2> Since you like <span class='red'>{fav_movie}</span> you may also like:<h2>", unsafe_allow_html=True)
st.image(item_based_movies_df["image_url"].to_list(), width=120, caption=item_based_movies_df["title"].to_list())

# # User based 
st.markdown(f"<h2> The User with the ID <span class='red'>{user_id}</span> might also like:<h2>", unsafe_allow_html=True)
st.dataframe(user_based_movies_df)
#st.image(user_based_movies_df["image_url"].to_list(), width=120, caption=user_based_movies_df["title"].to_list())
