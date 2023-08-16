import os
import pandas as pd
from flask import Flask, request, jsonify
app = Flask(__name__)   # Flask constructor

os.environ['KAGGLE_USERNAME'] = 'xxxx'
os.environ['KAGGLE_KEY'] = 'xxxxx'

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

def get_file_from_kaggle(dataset_value, select):
    dataset = str(dataset_value)
    file_name = str(select)
    path = f'./{select}'
    try:
        api.dataset_download_files(dataset, file_name, path, unzip=True)
    except Exception as e:
        print(e)
    csv_file = f'{select}/{select}'
    return pd.read_csv(csv_file)

@app.route("/get-kaggle-data/<path:dataset_value>", methods=["GET"])
def get_kaggle_data(dataset_value):
    try:
        select = request.args.get("select")
        if select:
            df = get_file_from_kaggle(dataset_value, select)
            df.drop(['X', 'Y', 'TELEPHONE', 'NAICS_CODE', 'NAICS_DESC', 'SOURCE', 'WEBSITE', 'SHELTER_ID'], axis=1)
            df.rename(columns = {'OBJECTID':'SCHOOL_ID', 'NCESID':'UNIVERSITY_NO', 'COUNTY':'TERITORRY', 'COUNTYFIPS':'TERITORRY_CODE', 'FT_TEACHER':'TEACHER_CODE'}, inplace = True)
            df.dropna(inplace=True)
            dropIndex = df[(df['STATE'] == 'DE') | (df['STATE'] == 'HI') | (df['STATE'] == 'KS') | (df['STATE'] == 'ME') | (df['STATE'] == 'ND') | (df['STATE'] == 'RI') | (df['STATE'] == 'WY') | (df['STATE'] == 'MS') | (df['STATE'] == 'ME') | (df['STATE'] == 'MT') | (df['STATE'] == 'NE') | (df['STATE'] == 'SD')].index
            print(dropIndex)
            df.drop(dropIndex, inplace = True)
            df.drop_duplicates(inplace = True)
            df = df[:1000]
            print(df.info())
            return df.to_json(orient="records")
        else:
            return jsonify({'error': 'Missing "select" parameter'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
  
if __name__=='__main__':
   app.run(debug = True)



   
