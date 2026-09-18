import pandas as pd
import matplotlib.pyplot as plt

# Load the scraped dataset
df = pd.read_csv("scraped_books.csv")

# Display basic information
print("Dataset loaded successfully!")
print("Number of books:", len(df))
print("Number of columns:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# -----------------------------
# Clean the Price column
# -----------------------------

# Remove currency symbols and other non-numeric characters
df["Price"] = df["Price"].astype(str).str.replace(
    r"[^\d.]",
    "",
    regex=True
)

# Convert Price into numeric values
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# -----------------------------
# Convert ratings into numbers
# -----------------------------

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating_Number"] = df["Rating"].map(rating_map)

# -----------------------------
# Price Analysis
# -----------------------------

print("\nAverage book price: £", round(df["Price"].mean(), 2))
print("Minimum book price: £", round(df["Price"].min(), 2))
print("Maximum book price: £", round(df["Price"].max(), 2))

# -----------------------------
# Rating Analysis
# -----------------------------

print("\nAverage rating:", round(df["Rating_Number"].mean(), 2))

print("\nRating distribution:")
print(df["Rating"].value_counts())

# -----------------------------
# Availability Analysis
# -----------------------------

print("\nAvailability:")
print(df["Availability"].value_counts())

# -----------------------------
# Most Expensive Books
# -----------------------------

print("\nTop 10 most expensive books:")

print(
    df[["Title", "Price", "Rating"]]
    .sort_values(by="Price", ascending=False)
    .head(10)
)

# -----------------------------
# Highest Rated Books
# -----------------------------

print("\nTop rated books:")

print(
    df[df["Rating_Number"] == 5][
        ["Title", "Price", "Rating"]
    ].head(10)
)

# ==================================================
# VISUALIZATION 1: Rating Distribution
# ==================================================

rating_counts = df["Rating"].value_counts()

rating_order = [
    "One",
    "Two",
    "Three",
    "Four",
    "Five"
]

rating_counts = rating_counts.reindex(
    rating_order
).fillna(0)

plt.figure(figsize=(8, 5))

rating_counts.plot(kind="bar")

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()

# ==================================================
# VISUALIZATION 2: Price Distribution
# ==================================================

plt.figure(figsize=(8, 5))

df["Price"].plot(
    kind="hist",
    bins=15
)

plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# ==================================================
# VISUALIZATION 3: Price vs Rating
# ==================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Rating_Number"],
    df["Price"]
)

plt.title("Book Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")

plt.tight_layout()
plt.savefig("price_vs_rating.png")
plt.show()

print("\nAnalysis completed successfully!")