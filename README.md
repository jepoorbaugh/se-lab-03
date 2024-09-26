# se-lab-03: Quote App
Software Engineering project to apply automated testing to backend web development

Basic app to display a daily inspirational quote to the user. Also has pages to display quotes with a specific tag a random quote.  

Uses a table of quotes compiled by [Kaggle user manann](https://www.kaggle.com/datasets/manann/quotes-500k). The set was filtered to only include the top 1000 most popular categories, and only quotes that contained at least 4 of these categories. This was done both to reduce the overall file size to allow the dataset to be uploaded to Github without dealing with large file storage, filter the dataset for uncategorized/poorly-categorized quotes, and limit the overall number of categories to something more reasonable. There are now around 100k quotes compared to the original 500k. 

# Requirements
- Use Flask to implement the backend for a web application
- The backend should serve at least 3 distinct pages via GET requests
    - Pages must include some form of dynamic content generated on the server side. This does not need to be overly complicated and can simply be basic math.
    - Pages should be valid HTML that renders correctly on all modern browsers
    - Pages should include links to one another
    - Pages can be brutalist (JS and CSS should not be used)

- Each page should have at least one test. Flask includes a simple testing framework
    - Tests should run automatically for each commit using Github Actions.
    - Tests should correctly test the functionality of your page. If the page is broken, the test should fail.

## Practices
Continue to follow appropriate software engineering practices including:
- Regular commits
- Appropriate commit messages
- Branches if needed or desired

# Design
Three Pages:
- `/`: Displays the same quote for 24 hours, then displays a new quote. The quote is chosen via the following:  
```python 
quote_list[(datetime.datetime.now() - datetime.datetime(1970,1,1)).days % len(quote_list)]
```
- `/topic/<topic>`: All quotes with topic `topic`
- `/author/<author>`: All quotes with author `author`

# Running Locally
## Step 1: Clone this Repository
Clone this repository wherever you want on your machine
```bash
git clone git@github.com:jepoorbaugh/se-lab-03.git
```

## Step 2: Install Flask
Follow the instructions on [Installing Flask](https://flask.palletsprojects.com/en/3.0.x/installation/)

## Step 3: Run application
Open your terminal and run: 
```bash
flask run
```
Make sure you do not do this in production! It is not safe!!
To run this in production, see [Flask's instructions](https://flask.palletsprojects.com/en/3.0.x/deploying/)

# Testing
Per the requirements, all pages must be tested.
- All tests should be in the "tests/test_pages.py"
- All tests should be run by Github Actions
Tests to be run on each page:
- `/`: Test to ensure the proper quote is displayed
- `/topic/<topic>`: Ensure the proper amount of quotes are displayed
- `/author/<author>`: Ensure the proper amount of quotes are displayed