import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv(r"C:\Users\anuka_b\OneDrive\Desktop\movie\tmdb_5000_credits.csv")

df["tags"] = df["genres"].fillna("")

cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(df["tags"]).toarray()

similarity = cosine_similarity(vectors)

def recommend(movie):
    idx = df[df["title"] == movie].index[0]
    distances = similarity[idx]

    movies = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [df.iloc[i[0]].title for i in movies]