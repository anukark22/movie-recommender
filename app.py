from flask import Flask, render_template, request
from model import recommend, df
from utils import fetch_poster
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    results = []

    if request.method == 'POST':
        movie = request.form['movie']
        recs = recommend(movie)

        for m in recs:
            results.append({
                "title": m,
                "poster": fetch_poster(m)
            })

    return render_template(
        'index.html',
        movies=df['title'].values,
        results=results
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)