import streamlit as st 
import pandas as pd
import pickle
import requests
similarity = pickle.load(open("similarity.pkl","rb"))

def fetch_poster(movies_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cb8b91e969cf599f5c4f8fa6ccd86cac&language=en-US'.format(movies_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    




def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distance = similarity[movie_index]
    movies_list =sorted(list(enumerate(distance)),reverse =True,key = lambda x : x[1])[1:6] 
    recommended_movies =[]
    recommende_movies_posters = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
        recommende_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommende_movies_posters
    





movies_dict = pickle.load(open("movies_dict.pkl","rb"))

movies =pd.DataFrame(movies_dict) 


st.title("Movie Reccomendation")

st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)



selectecmovie_name = st.selectbox(
    "What would yoou like to watch",
    movies["title"].values
)


if st.button("Recommend"):
    names,posters = recommend(selectecmovie_name)
    
    
    col1 ,col2, col3,col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])
    
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with  col5:
        st.text(names[4])
        st.image(posters[4])
   
