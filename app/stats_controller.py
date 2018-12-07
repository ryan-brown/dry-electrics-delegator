import json
from io import BytesIO

# import matplotlib.pyplot as plt
# import pandas as pd
import maya
from flask import Blueprint, render_template, jsonify, send_file

import database


stats = Blueprint('stats', __name__)

@stats.route("/", methods=['GET'])
def show_overview():
  try:
    """
    # 2748, 'Jon', 88, 0, '2018-11-26 23:03:01.044408-05:00'
    raw_data = database.select_everything()
    df = pd.DataFrame(data=raw_data, columns=['id', 'username', 'percentage', 'charging', 'updated_at'])
    # df = pd.read_csv('data.csv', parse_dates=['updated_at']) # uncomment to use a csv export instead of hitting the db
    del df['id']
    df.set_index('updated_at', inplace=True)
    # Drop outlier values
    df.drop(df.loc[df['username']=='jpham'].index, inplace=True)
    df.drop(df.loc[df['username']=='jmckenzie'].index, inplace=True)
    df.drop(df.loc[df['username']=='driest'].index, inplace=True)
    gdf = df.groupby('username')

    series = gdf['percentage'].plot(title="Charge Percentage over time", figsize=(len(df)/100,5))
    # TODO: add charging graph
    # axes = gdf['charging'].plot(title="Charge Status over time", subplots=True)

    plt.legend(loc='best')
    fig = plt.gcf()

    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='png')
    """
    return "WIP"
  except Exception as e:
    print(e)
    return "An unexpected error has occurred, please try again later", 500
