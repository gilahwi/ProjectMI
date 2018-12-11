import json
import os
import sys
import re
from urllib import request
from utils.wiktionaryparser import WiktionaryParser
from flask import Flask, render_template, request, redirect, url_for


# Initialize Flask instance
app = Flask(__name__)

# Use "query" variable from the URL. If no variable is given,
# use empty string instead. GET and POST methods are allowed.


@app.route("/search", defaults={"query": ""}, methods=["GET", "POST"])
@app.route("/search/<query>", methods=["GET", "POST"])



def search(query):
    
    processed_query = re.sub(r'[\W_]+',' ', query)
    queries = set(processed_query.split())
    t_all = []
    
    for query in queries:

        if request.method == "POST":
        # Get query from the POST form.
            query = request.form["query"]

        # Redirect to the same page with the query in the url.
        # ALWAYS REDIRECT AFTER POSTING!
            return redirect(url_for("search", query=query))

        parser = WiktionaryParser()

        json_list = parser.fetch(query.lower(), "Finnish")

        transdef = []
    
        try:
            if len(json_list) > 0:
                for item in json_list[0]["definitions"][0]["text"]:
                    transdef.append(item)
            else:
                transdef.append(None)
                            
        except:
            #ermsg = "We found nothing"
            #transdef.append(ermsg)
            print(None)

        if len(transdef) != 0:
            t_all.append(transdef)
        
        
    # Render finglish2.html with matches variable.
    return render_template("finglish2.html", transdef=transdef, t_all=t_all)
