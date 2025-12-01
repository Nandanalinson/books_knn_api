def recommend_knn(book_title, df, vectorizer, model, n_neighbors=5):

    if not book_title or book_title.strip() == "":
        return []

    title_vec = vectorizer.transform([book_title])
    distances, indices = model.kneighbors(title_vec, n_neighbors=n_neighbors+1)

    recommended_idx = indices[0][1:]
    recommendations = df.iloc[recommended_idx][["Book-Title", "Book-Author"]]

    return recommendations.to_dict(orient="records")
