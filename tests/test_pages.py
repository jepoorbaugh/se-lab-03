import pytest
import pandas as pd
import datetime
from app.quote_app import app


@pytest.fixture
def client():
    return app.test_client()


# @pytest.fixture
# def quote_data():
#     return pd.read_csv("filtered_quotes.csv")


def test_quote_of_the_day(client):
    """Test for the root page. Checks to see if the correct quote information is being displayed.

    Args:
        client (FlaskClient): the client to use to interact with the app
    """
    # Get quote information for today's date
    quote_data = pd.read_csv("filtered_quotes.csv")
    today_quote = (datetime.datetime.now() - datetime.datetime(1970, 1, 1)).days % len(
        quote_data
    )
    quote_info = quote_data.iloc[today_quote].to_dict()

    # Actually run tests
    response = client.get("/")
    assert quote_info["quote"].encode("UTF-8") in response.data
    assert quote_info["author"].encode("UTF-8") in response.data


def test_topic_page(client):
    # Pick a topic. e.g "love" and get all quotes with that topic/category
    quote_data = pd.read_csv("filtered_quotes.csv")
    topic = "love"

    category_quote_data = quote_data[
        # Categories are stored as a comma-delimited string, so we need to parse it.
        quote_data["category"].apply(lambda categories: topic in categories.split(", "))
    ].sort_values("author")

    first_result = category_quote_data.iloc[0].to_dict()

    # Assert we are telling the user the number of results, and displaying at least the first result.
    response = client.get(f"/topic/{topic}")
    assert str(len(category_quote_data)).encode("UTF-8") in response.data
    assert first_result["quote"].encode("UTF-8") in response.data
    assert first_result["author"].encode("UTF-8") in response.data
