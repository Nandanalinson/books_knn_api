from flask import Flask, jsonify, render_template, request
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)


model_data = pickle.load(open("data/recommender.pkl", "rb"))
pt = model_data["pt"]
similarity_scores = model_data["similarity_scores"]
books = model_data["book"]


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get_similar", methods=["POST"])
def get_similar():
    data = request.get_json(silent=True)
    book_name = data.get("book_name")

    recommendations = recommend(book_name)

    return jsonify({"recommendations": recommendations})

def recommend(book_title):
    index = np.where(pt.index == book_title)[0][0]
    distances = sorted(list(enumerate(similarity_scores[index])), reverse=True, key=lambda x: x[1])
    
    for i in distances[1:6]:
        print(pt.index[i[0]])

if __name__ == "__main__":
    app.run(debug=True)
