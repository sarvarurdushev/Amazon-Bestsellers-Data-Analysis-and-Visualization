# Amazon-Bestsellers-Data-Analysis-and-Visualization
This project analyzes the Amazon Bestsellers dataset using Python. The goal is to uncover trends among top authors, genres, and book ratings from 2009 to 2019. We use pandas for data handling and matplotlib for visualization.
# 📚 Amazon Bestsellers Data Analysis

This project analyzes the Amazon Bestsellers dataset using Python. It explores trends among top authors, book ratings, and genre popularity from 2009 to 2019. The analysis uses `pandas` for data processing and `matplotlib` for visualizations.


## 📦 Step-by-Step Explanation

### 1. Importing Libraries

```
import pandas as pd  
import matplotlib.pyplot as plt
```

We import pandas for data manipulation and matplotlib.pyplot for creating charts.

# 2. Loading the Dataset
Load the dataset from the CSV file into a pandas DataFrame:

```
df = pd.read_csv('bestsellers.csv')
```
# 3. Data Cleaning and Preprocessing
We clean and preprocess the data by removing duplicates, renaming columns, and ensuring proper data types:

```
df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
df["Price"] = df["Price"].astype(float)
```
# 4. Top 50 Authors by Number of Books
We identify the top 50 authors who appeared most frequently in the bestseller list:

```
author_counts = df['Author'].value_counts()
top_50_authors = author_counts.head(50)
```
# 5. Average Rating by Author
Calculate the average rating for each author:

```
avg_rating_by_author = df.groupby("Author")["Rating"].mean()
```
# 6. Top 5 Genres by Number of Books
Find the top 5 genres based on the number of books:

```
genre_counts = df['Genre'].value_counts()
top_5_genres = genre_counts.head(5)
```
### 📊 Visualizations
# 📌 1. Top 50 Authors by Number of Books
Bar chart showing the top 50 authors with the most books:

```
plt.figure(figsize=(12, 6))
top_50_authors.plot(kind='bar', color='blue', title='Top 50 Authors by Number of Books')
plt.xlabel('Author')
plt.ylabel('Number of Books')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
```
# 📌 2. Average Rating by Author
Bar chart showing the highest-rated authors (top 50):

```plt.figure(figsize=(12, 6))
avg_rating_by_author.sort_values(ascending=False).head(50).plot(kind='bar', color='green', title='Average Rating by Author')
plt.xlabel('Author')
plt.ylabel('Average Rating')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
```
# 📌 3. Top 5 Genres by Number of Books
Bar chart displaying the top 5 most common genres:

```
plt.figure(figsize=(8, 5))
top_5_genres.plot(kind='bar', color='orange', title='Top 5 Genres by Number of Books')
plt.xlabel('Genre')
plt.ylabel('Number of Books')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```
## 🚀 How to Run
Prerequisites
Make sure you have Python installed and run the following to install required packages:

```
pip install pandas matplotlib
```

Clone this repository:

```
git clone https://github.com/yourusername/amazon-bestsellers-analysis.git
cd amazon-bestsellers-analysis
```
Add the bestsellers.csv file to the same folder.

Run the script:
```
python analysis.py
```
