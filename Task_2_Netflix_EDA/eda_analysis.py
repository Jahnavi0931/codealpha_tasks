import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Load the Netflix dataset
# --------------------------------------------------

url = "https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/netflix_titles.csv"

df = pd.read_csv(url)

# --------------------------------------------------
# 2. Basic Dataset Information
# --------------------------------------------------

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Column Names ---")
print(df.columns)

print("\n--- Dataset Information ---")
df.info()

# --------------------------------------------------
# 3. Missing Values
# --------------------------------------------------

print("\n--- Missing Values ---")
print(df.isnull().sum())

# --------------------------------------------------
# 4. Duplicate Records
# --------------------------------------------------

print("\n--- Duplicate Rows ---")
print("Duplicate rows:", df.duplicated().sum())

# --------------------------------------------------
# 5. Movies vs TV Shows
# --------------------------------------------------

print("\n--- Movies vs TV Shows ---")
type_counts = df["type"].value_counts()
print(type_counts)

# --------------------------------------------------
# 6. Release Year Analysis
# --------------------------------------------------

print("\n--- Top 10 Release Years ---")
print(df["release_year"].value_counts().head(10))

# --------------------------------------------------
# 7. Genre Analysis
# --------------------------------------------------

print("\n--- Top 10 Genres ---")

genres = df["listed_in"].str.split(", ").explode()

top_genres = genres.value_counts().head(10)

print(top_genres)

# --------------------------------------------------
# 8. Country Analysis
# --------------------------------------------------

print("\n--- Top 10 Countries ---")

countries = df["country"].dropna().str.split(", ").explode()

top_countries = countries.value_counts().head(10)

print(top_countries)

# --------------------------------------------------
# 9. Rating Analysis
# --------------------------------------------------

print("\n--- Top 10 Ratings ---")

top_ratings = df["rating"].value_counts().head(10)

print(top_ratings)

# --------------------------------------------------
# 10. Duration Analysis
# --------------------------------------------------

movies = df[df["type"] == "Movie"].copy()

movies["duration_minutes"] = (
    movies["duration"]
    .str.replace(" min", "", regex=False)
    .astype(float)
)

average_duration = movies["duration_minutes"].mean()

print("\n--- Average Movie Duration ---")
print("Average movie duration:", round(average_duration, 2), "minutes")

# --------------------------------------------------
# 11. Movies vs TV Shows by Release Year
# --------------------------------------------------

year_type = (
    df.groupby(["release_year", "type"])
    .size()
    .unstack(fill_value=0)
)

print("\n--- Movies vs TV Shows by Year ---")
print(year_type.tail(10))

# --------------------------------------------------
# 12. Visualization 1: Movies vs TV Shows
# --------------------------------------------------

plt.figure()

type_counts.plot(kind="bar")

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.savefig("charts/movies_vs_tvshows.png")
plt.show()


# --------------------------------------------------
# 13. Visualization 2: Release Year Trend
# --------------------------------------------------

year_type = year_type.loc[2010:2019]

plt.figure()

year_type.plot(kind="line")

plt.title("Netflix Movies and TV Shows by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.savefig("charts/release_year_trend.png")
plt.show()

# --------------------------------------------------
# 14. Visualization 3: Top Genres
# --------------------------------------------------

plt.figure()

top_genres.plot(kind="bar")

plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig("charts/top_genres.png")
plt.show()

# --------------------------------------------------
# 15. Visualization 4: Top Countries
# --------------------------------------------------

plt.figure()

top_countries.plot(kind="bar")

plt.title("Top 10 Countries by Netflix Titles")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig("charts/top_countries.png")
plt.show()

# --------------------------------------------------
# 16. Visualization 5: Top Ratings
# --------------------------------------------------

plt.figure()

top_ratings.plot(kind="bar")

plt.title("Top 10 Netflix Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("charts/top_ratings.png")
plt.show()

# --------------------------------------------------
# 17. Visualization 6: Movie Duration Distribution
# --------------------------------------------------

plt.figure()

plt.hist(movies["duration_minutes"], bins=20)

plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")

plt.tight_layout()
plt.savefig("charts/movie_duration.png")
plt.show()


# Top 10 release years

top_years = df["release_year"].value_counts().head(10)

plt.figure(figsize=(10, 5))
top_years.sort_index().plot(kind="bar")

plt.title("Top 10 Release Years")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("charts/top_release_years.png")
plt.show()