import json
import os
import sys
from .utils.wiktionaryparser import WiktionaryParser
from flask import Flask, render_template, request, redirect, url_for


# Initialize Flask instance
app = Flask(__name__)

# Use "query" variable from the URL. If no variable is given,
# use empty string instead. GET and POST methods are allowed.


@app.route("/search", defaults={"query": "stop"}, methods=["GET", "POST"])
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
    transdef = []
    try:
        if len(json_list) == 0:
            ermsg = "We found nothing"
            transdef.append(ermsg)
        elif len(json_list) > 0:
            # pos = json.dumps(json_list[0]["definitions"][0]["partOfSpeech"])
            for item in json_list[0]["definitions"][0]["text"]:
                transdef.append(item)
    except:
        ermsg = "We found nothing"
        transdef.append(ermsg)

    # Render finglish.html with matches variable.
    return render_template("finglish.html", transdef=transdef)
