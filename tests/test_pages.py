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
