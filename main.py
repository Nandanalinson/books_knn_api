import pandas as pd

books = pd.read_csv("data/Books.csv")
ratings = pd.read_csv("data/Ratings.csv")
users = pd.read_csv("data/Users.csv")

print(books.shape)
print(ratings.shape)
print(users.shape)
