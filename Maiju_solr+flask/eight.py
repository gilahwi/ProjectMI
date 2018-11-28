from flaskwiki import Flask, render_template, request, redirect, url_for
from urllib.request import *

#Initialize Flask instance
app = Flask(__name__)

#Use "query" variable from the URL. If no variable is given,
#use empty string instead. GET and POST methods are allowed.
@app.route("/search", defaults={"query": ""}, methods=["GET", "POST"])
@app.route("/search/<query>", methods=["GET", "POST"])
def search(query):

    if request.method == "POST":
        #Get query from the POST form.
        query = request.form["query"]
        print(query)
        
        #Redirect to the same page with the query in the url.
        #ALWAYS REDIRECT AFTER POSTING!
        return redirect(url_for("search", query=query))

    matches = []

    #If an entry name contains the query, add the entry to matches.
    if query != "":
        url_string = "http://localhost:8983/solr/wiki/select?q=text:"+query+"&wt=python&start=0&rows=100"
        connection = urlopen(url_string)
        response = eval(connection.read())


        for i, document in enumerate(response['response']['docs']):
              #print("  Document title ", i, "=", document['title'])
            matches.append("  Document title " + str(i) + "=" + document['title'])
 
    #Render index.html with matches variable. 
    return render_template("index_solr.html", matches=matches)

