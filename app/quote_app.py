from flask import Flask
from flask import render_template, url_for, request, redirect
import pandas as pd
from random import randint
import datetime

app = Flask(__name__)


quote_data = pd.read_csv("filtered_quotes.csv")
categories = quote_data["category"].apply(lambda x: x.split(", ")).explode().unique()
authors = quote_data["author"].unique()


@app.route("/", methods=["GET", "POST"])
def quote_of_the_day():
    if request.method == "GET":
        # Get quote of the day
        quote_index = (
            datetime.datetime.now() - datetime.datetime(1970, 1, 1)
        ).days % len(quote_data)
        quote_info = quote_data.iloc[quote_index].to_dict()
        return render_template(
            "index.html",
            quote=quote_info["quote"],
            author=quote_info["author"],
            topic_options=categories,
            author_options=authors,
        )
    elif request.method == "POST":
        # Deal with redirecting users
        if "topic" in request.form.keys():
            return redirect(url_for("topic_page", topic=request.form["topic"]))
        elif "author" in request.form.keys():
            return redirect(url_for("author_page", author=request.form["author"]))


@app.route("/topic/<topic>")
def topic_page(topic):
    # Get quotes with topic
    category_quote_data = quote_data[
        # Categories are stored as a comma-delimited string, so we need to parse it.
        quote_data["category"].apply(lambda categories: topic in categories.split(", "))
    ].sort_values("author")

    return render_template(
        "quote_list.html",
        topic_options=categories,
        author_options=authors,
        num_results=len(category_quote_data),
        topic=topic,
        quotes=category_quote_data.to_records(),
    )


@app.route("/author/<author>")
def author_page(author):
    # Get quotes by author
    author_quote_data = quote_data[quote_data["author"] == author].sort_values("author")

    return render_template(
        "quote_list.html",
        topic_options=categories,
        author_options=authors,
        num_results=len(author_quote_data),
        topic=author,
        quotes=author_quote_data.to_records(),
    )
