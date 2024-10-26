

# Music Trend Prediction

## Project Overview
The **Music Trend Prediction** project aims to forecast song streams and popularity on streaming platforms like Spotify using machine learning. By analyzing factors such as artist information, track metadata, and social engagement, this project helps artists, producers, and marketers better understand and anticipate music trends, making it possible to make data-driven decisions in the music industry.

## Motivation
The music industry is increasingly data-driven, with digital streaming platforms providing vast amounts of data. This project addresses the need for:
- **Trend Forecasting:** Predicting which songs or artists will trend based on historical data.
- **Cross-Platform Insights:** Utilizing data from multiple sources (Spotify, YouTube) to provide a comprehensive view.
- **Data-Driven Decision Making:** Enabling targeted marketing and optimized content creation based on predictive insights.

## Project Objectives
1. **Analyze Streaming Data:** Identify emerging genres, artists, and songs by analyzing data from Spotify and YouTube.
2. **Predict Song Popularity and Streams:** Forecast metrics like views and follower engagement using various ML models.
3. **Utilize Cultural and Social Insights:** Consider external factors like social events and cultural trends that influence music popularity.

## Data Sources
The data for this project is gathered from:
- **Spotify API:** To collect song metadata, audio features, artist information, and streaming data.
- **YouTube API & Third-Party Sources:** Used to capture view counts, like counts, and other engagement metrics.
- **Additional Sources:** Such as kworb.net for supplementary streaming statistics where API data is unavailable.

## Key Features
- **Data Cleaning & Preprocessing:** Standardizes data collected from multiple sources, normalizes fields, and handles missing data.
- **Exploratory Data Analysis (EDA):** Correlates factors like artist followers, song genre, and other features with popularity.
- **Machine Learning Models:** Uses Random Forest, XGBoost, and ensemble models to predict song popularity and streams.
- **Cross-Platform Prediction:** Merges Spotify and YouTube data to offer comprehensive insights across platforms.

## Methodology
1. **Data Collection:** Retrieve streaming and engagement data from Spotify and YouTube.
2. **Data Preprocessing:** Clean, merge, and normalize data from different sources.
3. **Exploratory Data Analysis (EDA):** Identify trends, correlations, and important features.
4. **Model Training:** Train machine learning models on key features.
5. **Model Evaluation:** Evaluate models using metrics like Mean Squared Error (MSE) and R-squared scores.
6. **Interpretation & Visualization:** Provide visual insights on prediction results.

