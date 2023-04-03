import streamlit as st
import pandas as pd
import altair as alt

# Load data from CSV to a pandas dataframe

def load_data():
    return pd.read_csv("movie_ratings.csv")

# Page title
st.title("Monitoring the Movie Ratings and Recommendation System")

# Load data
df = load_data()

# Define color range
range_colors = ['steelblue', 'lightgray', '#aec7e8', '#ffbb78', '#2ca02c']

# Create a color encoding for ratings
rating_color = alt.Color('ratings', scale=alt.Scale(domain=['1', '2', '3', '4', '5'], range=range_colors))

# Create a bar chart of movie ratings
rating_counts = df['ratings'].value_counts().sort_index() 
chart = alt.Chart(rating_counts.reset_index()).mark_bar().encode(
    x=alt.Y('index:O', axis=alt.Axis(title='Rating'), sort='-x'),
    y=alt.X('ratings:Q', axis=alt.Axis(title='Number of Ratings')),
)
st.write("Movie rating distribution:")
st.altair_chart(chart, use_container_width=True)


# Create a scatter plot of movie ratings over time
df['timestamp'] = pd.to_datetime(df['timestamp'])
chart = alt.Chart(df).mark_circle(size=60).encode(
    x=alt.X('timestamp', axis=alt.Axis(title='Timestamp')),
    y=alt.Y('ratings', axis=alt.Axis(title='Rating')),
    tooltip=['movie_id'],
    color=rating_color
).interactive()
st.write("Movie rating over time:")
st.altair_chart(chart, use_container_width=True)



# Display the data in a table
st.write("Movie ratings data:")
st.write(df)

st.markdown("<h3 style='color: #FF00FF; font-weight: bold;'>Get details of a random movie rating</h3>", unsafe_allow_html=True)
if st.button("Get random rating"):
    mini_df = df.head(1000)
    movie = mini_df.sample(n=1).iloc[0]
    st.write(f"""The movie {movie['movie_id']} has a rating of {movie['ratings']} given by user {movie['user_id']} at {movie['timestamp']}""")

footer_container = st.container()


footer_container.markdown(
    f'<p style="font-family: cursive; font-size: 20px; text-align: center;">This page is created by Pratik Mandlecha</p>',
    unsafe_allow_html=True
)