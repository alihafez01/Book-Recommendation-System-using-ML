# Book Recommendation System using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-orange)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0%2B-yellowgreen)
![License](https://img.shields.io/badge/License-MIT-green)

This project is a **Book Recommendation System** that suggests books based on user preferences. It uses a dataset of books, their ratings, and other metadata to recommend similar books using a **k-nearest neighbors (KNN)** algorithm.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
The Book Recommendation System analyzes a dataset of books and their metadata (e.g., ratings, authors, number of pages) to recommend books similar to a given book. It uses the following steps:
1. **Data Preprocessing**: Cleans and prepares the dataset for analysis.
2. **Feature Engineering**: Creates features like rating bins and one-hot encoding for categorical variables.
3. **Model Training**: Uses the KNN algorithm to find similar books based on features.
4. **Recommendation**: Recommends books based on the nearest neighbors of a given book.

---

## Features
- **Data Exploration**: Visualizes the dataset to understand book ratings, authors, and more.
- **KNN Algorithm**: Finds similar books based on metadata.
- **Modular Code**: Organized into separate modules for preprocessing, training, and recommendation.
- **Easy to Use**: Simple command-line interface to get recommendations.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Book-Recommendation-System-using-ML.git
   cd Book-Recommendation-System-using-ML
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Place your dataset (`books.csv`) in the `data/raw/` folder.

2. Run the main script to get book recommendations:
   ```bash
   python main.py
   ```

3. Example output:
   ```python
   ['Harry Potter and the Half-Blood Prince (Harry Potter #6)', 
    'Harry Potter and the Order of the Phoenix (Harry Potter #5)', 
    'The Fellowship of the Ring (The Lord of the Rings #1)', 
    'Harry Potter and the Chamber of Secrets (Harry Potter #2)', 
    'Harry Potter and the Prisoner of Azkaban (Harry Potter #3)', 
    'The Lightning Thief (Percy Jackson and the Olympians #1)']
   ```

---

## Project Structure

```
Book-Recommendation-System-using-ML/
│
├── data/
│   ├── raw/            # Raw datasets like books.csv
│   ├── processed/      # Processed datasets (if any)
│
├── src/
│   ├── preprocess.py   # Data cleaning and preprocessing
│   ├── model.py        # KNN model and recommendation logic
│   ├── visualize.py    # Data visualization scripts
│   ├── main.py         # Main script for execution
│
├── requirements.txt    # Required Python libraries
└── README.md           # Project overview
```

---

## Dataset
The dataset used in this project is `books.csv`, which contains the following columns:

- `title`: Title of the book.
- `authors`: Author(s) of the book.
- `average_rating`: Average rating of the book.
- `ratings_count`: Number of ratings the book has received.
- `num_pages`: Number of pages in the book.
- `language_code`: Language of the book.

You can replace this dataset with your own by placing it in the `data/raw/` folder.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.


