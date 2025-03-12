import pandas as pd
from src.data_preprocessing import preprocess_data
from src.model_training import train_model
from src.recommender import book_recommender

# Load data
try:
    df = pd.read_csv('Data/raw/books.csv', on_bad_lines='skip')  # For Pandas 1.3.0+
except Exception as e:
    print(f"Error loading CSV file: {e}")
    exit()

# Preprocess data
features = preprocess_data(df)

# Train model and get idlist
model, idlist = train_model(features)

# Get recommendations
recommendations = book_recommender(df, model, idlist, 'Harry Potter and the Half-Blood Prince (Harry Potter  #6)')
print(recommendations)