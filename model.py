import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("C:\\Users\\anuka_b\\OneDrive\\Desktop\\movie\\tmdb_5000_credits.csv")

# flexible tags
if 'genres' in df.columns:
    df['tags'] = df['genres']
elif 'overview' in df.columns:
    df['tags'] = df['overview']
else:
    df['tags'] = df.iloc[:, 1]

df['tags'] = df['tags'].fillna('')

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(df['tags']).toarray()

similarity = cosine_similarity(vectors)


def recommend(movie):
    if movie not in df['title'].values:
        return []

    idx = df[df['title'] == movie].index[0]
    distances = similarity[idx]

    movies = sorted(list(enumerate(distances)),
                    reverse=True,
                    key=lambda x: x[1])[1:6]

    results = []
    for i in movies:
        results.append(df.iloc[i[0]].title)

    return results