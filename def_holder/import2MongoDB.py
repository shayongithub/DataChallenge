import sys
import pandas as pd
import pymongo
import json
import os

def import_content(filepath):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['diemthi'] #Replace mongo db name
    collection_name = 'finalAssignment' #Replace mongo db collection name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

if __name__ == "__main__":
  filepath = '/result.csv'  # pass usedcsv file path
  import_content(filepath)
  print('Import successfully. Check your MongoDB !')