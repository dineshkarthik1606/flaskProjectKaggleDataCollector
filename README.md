# flaskProjectKaggleDataCollector

This app is used to fetch data from Kaggle and expose it as a json format.

Follow the below instructions to get kaggle api token.

Sign up for https://www.kaggle.com
Goto Settings from Profile button.
Click Create new Token under Api section.
Replace the generated token and username in app.py file.

You can change the dataset and the file by calling throught the api. For example http://127.0.0.1:5000/get-kaggle-data/andrewmvd/us-schools-dataset?select=Private_Schools.csv

For deploying to Heroku server use the following content in a Procfile, then create an app in Heroku CLI and link with Github repo and deploy.
web: gunicorn app:app
