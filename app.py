import streamlit as st
st.title("Guy burac project")
import kagglehub
import pandas as pd
path = kagglehub.dataset_download("rush4ratio/video-game-sales-with-ratings")
print("Path to dataset files:", path)
df = pd.read_csv(path + "/Video_Games_Sales_as_at_22_Dec_2016.csv")
df.head()
