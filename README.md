# 📊 CORD-19 Data Explorer

This project explores the CORD-19 metadata dataset and builds a simple Streamlit app for interactive visualization.

## Dataset
The original `metadata.csv` from the CORD-19 dataset is over 1.5 GB, which exceeds GitHub’s file size limit.  
For this project, we include a smaller sample: `metadata_sample.csv` (5,000 rows).  

If you want the full dataset, download it from Kaggle:  
👉 https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge


## 🔹 Features
- Load and clean CORD-19 metadata
- Explore publications by year, journal, and title keywords
- Interactive year filtering
- Word cloud of research paper titles
- Streamlit web application

## 🔹 Tools
- Python 3.7+
- pandas
- matplotlib / seaborn
- wordcloud
- streamlit

## 🔹 How to Run
1. Clone this repo:
   ```bash
git clone https://github.com/KIRUMAH-sam/wk-8_FrameworksPy.git
cd wk-8_FrameworksPy

## Experience 
~The experience with this data analysis in python was one very stressing requires attention to detail constant debugging and patience.
Challenges occured while load and making a sample data frame there after the analysis was smooth until the addition of the framework streamlit.
All in all it was a good exercise!
