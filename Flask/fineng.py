import json
import os
import sys
from .utils.wiktionaryparser import WiktionaryParser
from flask import Flask, render_template, request, redirect, url_for


# Initialize Flask instance
app = Flask(__name__)

# Use "query" variable from the URL. If no variable is given,
# use empty string instead. GET and POST methods are allowed.


@app.route("/search", defaults={"query": "kissa"}, methods=["GET", "POST"])
@app.route("/search/<query>", methods=["GET", "POST"])
def search(query):

    if request.method == "POST":
        # Get query from the POST form.
        query = request.form["query"]

        # Redirect to the same page with the query in the url.
        # ALWAYS REDIRECT AFTER POSTING!
        return redirect(url_for("search", query=query))

    parser = WiktionaryParser()
    json_list = parser.fetch(query, "Finnish")

    pos = json.dumps(json_list[0]["definitions"][0]["partOfSpeech"])
    transdef = []

    for item in json_list[0]["definitions"][0]["text"]:
        transdef.append(item)

    print(query)
    print("pos" + pos)
    for item in transdef:
        print(item)

    # Render finglish.html with matches variable.
    return render_template("finglish.html")
