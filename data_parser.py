import numpy as np
import pandas as pd
import os
import json
from datetime import datetime



def pulldata():
    i = 0
    df = pd.DataFrame(columns=['track','artist','time','ms','uri','skipped'])
    dir = os.getcwd()
    for filename in os.listdir(dir+'/data'):
        if "endsong_" in filename:
            print(f'Reading filename: {filename}')
            with open('data/'+filename) as f:
                data = json.load(f)
                array = []
                for row in data:
                    date = datetime.strptime(row['ts'],"%Y-%m-%dT%H:%M:%SZ")
                    row_data = [row['master_metadata_track_name'],row['master_metadata_album_artist_name'],date,row['ms_played'],row['spotify_track_uri'],row['skipped']]
                    array.append(row_data)
                array = pd.DataFrame(np.array(array), columns=['track','artist','time','ms','uri','skipped'])
                df = pd.concat([df,array], axis = 0)
    df.to_csv('data/all.csv', index=False, encoding='utf-8')
    return df

def get_data():
    if os.path.isfile(os.getcwd()+"/data/all.csv"):
        df = pd.read_csv('data/all.csv')
        return df
    return pulldata()