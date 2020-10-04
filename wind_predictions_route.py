from flask import Flask, jsonify, request, make_response, render_template, request, redirect, url_for, abort,send_from_directory
import pandas as pd
import numpy as np
import sklearn
import pickle
import json
import os



app= Flask(__name__)
@app.route("/predictions/wind", methods=["GET","POST"])


def wind_pred():

    #reading test data

    dp=pd.read_csv('Wind_api.csv')

    W1=dp.values


    model_name= ("wind_pickle_model.sav")

    loaded_model = pickle.load(open(model_name, 'rb'))

    try:

        wind_pred= loaded_model.predict(W1)

    except:

        return jsonify("Error occured while processing your data into our model!")

    print("done")

    response={'data':[],}

    return jsonify({'result': loaded_model.predict(W1)[0]}), 201

    response['data']=list(wind_pred)

    return make_response(jsonify(response),200)


if __name__=='__main__':

    app.run(debug=True)
