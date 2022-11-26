import pymongo
import pandas as pd 
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME="aps"
COLLECTION_NAME="sensor"
DATA_FIE_PATH="/config/workspace/aps_failure_training_set1.csv"


if __name__=="__main__":

    df=pd.read_csv(DATA_FIE_PATH)
    print(f"DF shape : {df.shape}")

    # convert DF to JSON to dump in mongo DB
    df.reset_index(drop=True,inplace=True)    
    json_record=list(json.loads(df.T.to_json()).values())

    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)