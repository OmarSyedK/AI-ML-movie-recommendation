import streamlit as st
import pickle
import pandas as pd
import requests
import time


def fetch_posters(movie_id):
    """Fetches a movie poster URL from the TMDB API given a movie ID."""
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = requests.get(
                f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8040b2f4f604c91a28e946a13ec5c7ee',
                timeout=5
            )
            response.raise_for_status()
            data = response.json()

            if 'poster_path' in data and data['poster_path']:
                return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
            else:
                # Return a placeholder if no poster is available
                return "https://placehold.co/500x750/374151/FFFFFF?text=No+Poster"
        except requests.exceptions.RequestException:

            if attempt < max_retries - 1:
                time.sleep(1) # Wait for 1 second before retrying
                continue
            else:
                st.error(f"Failed to fetch poster for movie ID {movie_id} after several retries.")
                return "https://placehold.co/500x750/374151/FFFFFF?text=Error"
    return "https://placehold.co/500x750/374151/FFFFFF?text=Error"

try:
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model files not found. Please make sure 'movies_dict.pkl' and 'similarity.pkl' are in the same directory.")
    st.stop()

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title('Movie Recommender System')

st.subheader("Select a movie you've enjoyed, and we'll suggest five similar ones!")

selected_movie_name = st.selectbox(
    '### **Which movie have you watched?**',
    movies['title'].values
)

if st.button('Recommend Movies', type="primary"):

    name = []
    posters = []
    loading_messages = [
        "Analyzing genres... 🎭",
        "Cross-referencing the cast... 🌟",
        "Consulting the directors... 🎥",
        "Evaluating keywords and tags... 🏷️",
        "Finalizing your recommendations! ✨"
    ]

    with st.spinner('Finding similar movies...'):
        loading_area = st.empty()

        movie_index = movies[movies['title'] == selected_movie_name].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        for i, movie_data in enumerate(movies_list):
            # Update the loading message and progress bar
            with loading_area.container():
                st.info(loading_messages[i])
                st.progress((i + 1) * 20)
                time.sleep(0.3)

            # Fetch movie details
            movie_id = movies.iloc[movie_data[0]].movie_id
            name.append(movies.iloc[movie_data[0]].title)
            posters.append(fetch_posters(movie_id))
            time.sleep(0.5)

        loading_area.empty() # Clear the loading messages

    st.success('Here are your movie recommendations!')

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(name[i])
            st.image(posters[i])