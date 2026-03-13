import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # 1. Load Data
    df = pd.read_csv('Netflix_data.csv')

    # 2. Data Cleaning
    # Addressing missing values
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')
    df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
    df['date_added'] = df['date_added'].fillna(df['date_added'].mode()[0])

    # 3. Data Exploration / Statistical Analysis
    print("General Data Description:")
    print(df.describe(include='all'))
    print("
Content Type Distribution:")
    print(df['type'].value_counts())

    # 4. Visualizations
    # a. Most watched genres (top 10)
    genres_series = df['listed_in'].str.split(', ')
    all_genres = genres_series.explode()
    top_genres = all_genres.value_counts().head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_genres.values, y=top_genres.index, palette='viridis')
    plt.title('Top 10 Most Watched Genres on Netflix')
    plt.xlabel('Count')
    plt.ylabel('Genre')
    plt.tight_layout()
    plt.savefig('top_genres.png')
    print("Saved: top_genres.png")

    # b. Ratings distribution
    rating_counts = df['rating'].value_counts()
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='rating', order=rating_counts.index, palette='magma')
    plt.title('Distribution of Content Ratings on Netflix')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('ratings_distribution.png')
    print("Saved: ratings_distribution.png")

if __name__ == "__main__":
    main()
