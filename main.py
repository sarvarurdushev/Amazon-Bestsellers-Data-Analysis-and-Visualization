# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv('bestsellers.csv')


# # Get the first 5 rows of the spreadsheet
# print(df.head())

# # Get the shape of the spreadsheet
# print(df.shape)

# # Get the column names of the spreadsheet
# print(df.columns)

# # Get summary statistics for each column
# print(df.describe())

# df.drop_duplicates(inplace=True)

# df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)


# df["Price"] = df["Price"].astype(float)

# author_counts = df['Author'].value_counts()
# print(author_counts)

# avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
# print(avg_rating_by_genre)


# # Export top selling authors to a CSV file
# author_counts.head(10).to_csv("top_authors.csv")

# # Export average rating by genre to a CSV file
# avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")


# # Plot author counts as a bar chart
# author_counts.head(10).plot(kind='bar', color='blue', title='Top 10 Authors by Book Count')
# plt.xlabel('Author')
# plt.ylabel('Book Count')
# plt.show()

# # Plot average rating by genre as a bar chart
# avg_rating_by_genre.plot(kind='bar', color='green', title='Average Rating by Genre')
# plt.xlabel('Genre')
# plt.ylabel('Average Rating')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('bestsellers.csv')

# Clean and preprocess the data
df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
df["Price"] = df["Price"].astype(float)

# Top 50 authors by the number of books
author_counts = df['Author'].value_counts()
top_50_authors = author_counts.head(50)

# Average rating by author
avg_rating_by_author = df.groupby("Author")["Rating"].mean()

# Top 5 genres by the number of books
genre_counts = df['Genre'].value_counts()
top_5_genres = genre_counts.head(5)

# Visualization

# Figure 1: Top 50 authors by the number of books (Bar Chart)
plt.figure(figsize=(12, 6))
top_50_authors.plot(kind='bar', color='blue', title='Top 50 Authors by Number of Books')
plt.xlabel('Author')
plt.ylabel('Number of Books')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Figure 2: Average rating by author (Bar Chart)
plt.figure(figsize=(12, 6))
avg_rating_by_author.sort_values(ascending=False).head(50).plot(kind='bar', color='green', title='Average Rating by Author')
plt.xlabel('Author')
plt.ylabel('Average Rating')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Figure 3: Top 5 genres by the number of books (Bar Chart)
plt.figure(figsize=(8, 5))
top_5_genres.plot(kind='bar', color='orange', title='Top 5 Genres by Number of Books')
plt.xlabel('Genre')
plt.ylabel('Number of Books')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()