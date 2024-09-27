from flask import Flask
from flask import render_template
import pandas as pd
from random import randint
import datetime

app = Flask(__name__)


quote_data = pd.read_csv("filtered_quotes.csv")


@app.route("/")
def quote_of_the_day():
    # Get quote of the day 
    quote_index = (datetime.datetime.now() - datetime.datetime(1970, 1, 1)).days % len(
        quote_data
    )
    quote_info = quote_data.iloc[quote_index].to_dict()
    return render_template(
        "index.html", quote=quote_info["quote"], author=quote_info["author"]
    )
