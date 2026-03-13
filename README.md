# Netflix_Data_Visualisation
Netflix Data Visualization using Python and R

Module 4 Assignment: Visual Analytics for Streaming Insights

Project Overview
As a developer at Netflix, this project involves cleaning, exploring, and visualizing a dataset of movies and TV shows. The goal is to provide stakeholders with actionable insights regarding content distribution, popular genres, and audience ratings using a combination of Python and R.

Tech Stack
Languages: Python 3.x, R

Python Libraries: Pandas (Data Manipulation), Matplotlib & Seaborn (Visualization)
R Libraries: ggplot2

File Structure
.
├── Netflix_shows_movies.csv        # Raw Dataset
├── Netflix_shows_movies_cleaned.csv# Processed Dataset
├── netflix_analysis.py             # Python Analysis Script
├── netflix_analysis.R              # R Visualization Script
├── top_genres.png                  # Exported Genre Chart
├── ratings_distribution.png        # Exported Ratings Chart
└── README.md                       # Documentation (This file)

Data Cleaning & Preparation
To ensure the integrity of the visual analytics, the following steps were taken:

Missing Values: * director, cast, and country contained null values which were noted to maintain data rows for general analysis.

rating and date_added were filled using the Mode (most frequent value) of their respective columns.

Dataset Renaming: The original file was handled and referenced as Netflix_shows_movies.

Key Insights
1. Most Watched Genres
The visualization highlights that International Movies, Dramas, and Comedies comprise the largest portion of Netflix's library.

2. Ratings Distribution
The distribution analysis shows a significant lean towards TV-MA and TV-14 content, suggesting that Netflix's primary target audience consists of adults and teenagers.

How to Run the Code
Python Environment

Install dependencies:
pip install pandas matplotlib seaborn
Run the analysis:
python netflix_analysis.py

R Environment
Ensure ggplot2 is installed:

R
install.packages("ggplot2")
Run the script to generate the integrated R chart:

R
source("netflix_analysis.R")

Statistical Summary
The data exploration phase included a df.describe() analysis which revealed:

Total entries: 6,234

Unique Titles: 6,172

Most frequent Release Year: 2018

Content split: Roughly 2/3 Movies and 1/3 TV Shows.

Developed by: [Precious Donald]

Assignment: Module 4 - Netflix Data Visualization
