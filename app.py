"""Main app"""
from flask import Flask, render_template
import os
import urllib.request, json


app = Flask(__name__)


# # Import env file if exists
if os.path.isfile('env.py'):
    import env


key = os.environ.get("API_KEY")
# secret = os.environ.get("API_SECRET")
# print(secret)
url = f"https://api.nytimes.com/svc/archive/v1/1987/1.json?api-key={key}"


# @app.route("/")
# def get_articles():
#     # url = f"https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key={key}"
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     data_dict = json.loads(data)

#     return render_template("articles.html", articles = data_dict["response"]["docs"])


@app.route("/")
def get_archives_list():
    # url = f"https://api.nytimes.com/svc/archive/v1/2019/1.json?api-key={key}"
    response = urllib.request.urlopen(url)
    data = response.read()
    data_dict = json.loads(data)

    articles = []
    for article in data_dict["response"]["docs"]:
        article = {
            "abstract": article["abstract"],
            "url": article["web_url"],
            "headline": article["headline"]["main"],
            "source": article["source"],
            "image": article["multimedia"]
        }
        articles.append(article)
        
    return render_template("articles.html", articles = articles)


if __name__ == "__main__":
    app.run(debug=True)
