# flaskProjectKaggleDataCollector
This app is used to fetch data from Kaggle and expose it as a json format.

Follow the below instructions to get kaggle api token.
1. Sign up for https://www.kaggle.com
2. Goto **Settings** from **Profile** button.
3. Click **Create new Token** under **Api** section.

Replace the generated token and username in **app.py** file.

You can change the dataset and the file by calling throught the api. For example http://127.0.0.1:5000/get-kaggle-data/andrewmvd/us-schools-dataset?select=Private_Schools.csv
