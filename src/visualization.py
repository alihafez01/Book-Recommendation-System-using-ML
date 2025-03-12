import seaborn as sns
import matplotlib.pyplot as plt

def plot_top_ten_books(df):
    top_ten = df[df['ratings_count'] > 1000000]
    top_ten.sort_values(by='average_rating', ascending=False)
    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize=(10, 10))
    data = top_ten.sort_values(by='average_rating', ascending=False).head(10)
    sns.barplot(x="average_rating", y="title", data=data, palette='inferno')
    plt.show()

