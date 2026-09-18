import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# Store scraped data
books = []

# Scrape first 5 pages
for page in range(1, 6):

    url = base_url.format(page)

    print(f"Scraping page {page}...")

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Could not access page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books on the page
    book_items = soup.select("article.product_pod")

    for book in book_items:

        # Book title
        title = book.h3.a["title"]

        # Price
        price = book.select_one(".price_color").text.strip()

        # Rating
        rating_class = book.select_one("p.star-rating")["class"]
        rating = rating_class[1]

        # Availability
        availability = book.select_one(".availability").text.strip()

        # Product URL
        book_link = book.h3.a["href"]

        if book_link.startswith("../"):
            book_link = book_link.replace("../", "")

        product_url = "https://books.toscrape.com/catalogue/" + book_link

        # Add information to our list
        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "URL": product_url
        })

# Convert data into a DataFrame
df = pd.DataFrame(books)

# Save data to CSV
df.to_csv("scraped_books.csv", index=False)

# Display results
print("\nScraping completed successfully!")

print(f"Total books scraped: {len(df)}")

print("\nFirst 10 books:")
print(df.head(10))

print("\nData saved as: scraped_books.csv")