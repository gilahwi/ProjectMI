# ProjectMI

This project is about building NLP applications

First, install Flask
https://github.com/miau1/flask-example

Then, install Wiktionary
https://github.com/Suyash458/WiktionaryParser

Then, move the Wiktionary files and directories into the flask-example directory. The wiktionaryparser.py file needs to be in the utils directory. Run fineng.py or fineng2.py with Flask. If you get a module not found error, try changing the "from .utils.wiktionaryparser import WiktionaryParser" to "from utils.wiktionaryparser import WiktionaryParser". 

There are two versions of the application: fineng.py takes in as input only one word, fineng2.py works with whole sentences. 
