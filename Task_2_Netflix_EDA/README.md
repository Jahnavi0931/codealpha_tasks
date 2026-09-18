# Task 2 - Netflix EDA
# Netflix Data Analysis

## CodeAlpha Data Analytics Internship

## Project Overview

This project performs Exploratory Data Analysis (EDA) on a Netflix titles dataset.

The goal is to understand the structure of the dataset, identify missing values and duplicate records, analyze patterns and trends, and create visualizations to communicate the findings clearly.

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- VS Code
- GitHub

## Dataset

The project uses a Netflix titles dataset containing information about movies and TV shows.

The dataset contains **6,234 titles and 12 columns**, including:

- Show ID
- Type
- Title
- Director
- Cast
- Country
- Date Added
- Release Year
- Rating
- Duration
- Genre
- Description

## Exploratory Data Analysis

The following analyses were performed:

- Movies vs TV Shows
- Release year distribution
- Top Netflix genres
- Top countries
- Content ratings
- Movie duration
- Missing value analysis
- Duplicate record analysis

## Key Findings

- The dataset contains **4,265 Movies** and **1,969 TV Shows**.
- Movies make up approximately **68.4%** of the dataset, while TV Shows make up approximately **31.6%**.
- **2018** had the highest number of titles by release year, with **1,063 titles**.
- **International Movies** was the most frequent category, with **1,927 occurrences**.
- The **United States** appeared most frequently as a country, with **2,609 occurrences**.
- **TV-MA** was the most common content rating, with **2,027 titles**.
- The average movie duration was approximately **99.1 minutes**.
- The dataset contains **0 duplicate rows**.
- Missing values were found mainly in the **Director, Cast, and Country** columns.
- The top release years show a large concentration of titles released in recent years, with **2018** having the highest count in the dataset.

## Visualizations

### 1. Movies vs TV Shows

![Movies vs TV Shows](charts/movies_vs_tvshows.png)

### 2. Release Year Trend

![Release Year Trend](charts/release_year_trend.png)

### 3. Top 10 Release Years

![Top Release Years](charts/top_release_years.png)

### 4. Top 10 Netflix Genres

![Top Genres](charts/top_genres.png)

### 5. Top 10 Countries

![Top Countries](charts/top_countries.png)

### 6. Top 10 Content Ratings

![Top Ratings](charts/top_ratings.png)

### 7. Movie Duration Distribution

![Movie Duration](charts/movie_duration.png)

## How to Run

To run this project, install the required Python libraries and run the Python file.

### Install the required libraries
run the project 
python eda_analysis.py

```bash
pip install pandas matplotlib
