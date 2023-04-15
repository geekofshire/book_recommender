import streamlit as st
import pickle
import numpy as np


popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))
count=0
def recommend(user_input):
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    return data

with st.sidebar:
    st.header("Book Reccomendation Website")
    b1=st.button("Top 50 Books")
    b2=st.button("Get your Reccomendation")
    st.write("Made by [Rohan Jha](https://github.com/geekofshire)")
    st.write("[Source Code](https://github.com/geekofshire/book_recommender)")

#st.write("Book Reccomedation Website")

#b1=st.button("Top 50 Books")
if b1:
    
    st.write("Top Books Reccomended by Users")
    for i in range(len(popular_df)):
        st.image(popular_df.iloc[i,2])
        st.write(popular_df.iloc[i,0],"by",popular_df.iloc[i][1])

input=st.selectbox("Select Book and click on get reccomendation button",options=list(popular_df["Book-Title"]),key=count)
if b2:
    list=recommend(str(input))
    count+=1
    for i in range(len(list)):
        st.image(list[i][2])
        st.write(list[i][0],"by",list[i][1])