# ProjectMI

ProjectMI - Finglish Terms is a translator from Finnish to English based on the Wiktionary data. 

It consists of two versions: fineng.py starts up a simple but fast translator, which handles just single word at a time, and fineng2.py starts up a more upgraded translator, which can handle collocations ans sentenses. 

Fineng2.py can be used as a 'lazy' dictionary for concrete text. It clears the input text from all the punctuation, removes duplicate words and outputs the results for each word in the alphabetical order.

## Installation

All working files for this project are located in the folder 'Flask'. 

Clone this repository on your computer.

Install Flask
https://github.com/miau1/flask-example

Install the latest Wiktionary dump file
https://dumps.wikimedia.org/enwiki/

Install WiktionaryParser
https://github.com/Suyash458/WiktionaryParser

Then, move the Wiktionary files and directories into the 'flask-example' directory. The wiktionaryparser.py file needs to be in the 'utils' directory. Run fineng.py or fineng2.py with Flask. If you get a 'module not found' error, try changing the "from .utils.wiktionaryparser import WiktionaryParser" to "from utils.wiktionaryparser import WiktionaryParser". 

