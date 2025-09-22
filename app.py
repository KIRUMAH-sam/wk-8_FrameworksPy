import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Load cleaned data
df = pd.read_csv("data/metadata_sample.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Interactive year filter
year_range = st.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write("### Sample Data", filtered[['title','authors','journal','year']].head())

# Publications by year
st.write("### Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
st.pyplot(fig)

# Top journals
st.write("### Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
st.pyplot(fig)

# Word cloud of titles
st.write("### Word Cloud of Titles")
text = " ".join(filtered['title'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400).generate(text)
fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
