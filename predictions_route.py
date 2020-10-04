from flask import Flask, flash, jsonify, request, make_response, render_template, request, redirect, url_for, abort,send_from_directory
from werkzeug.utils import secure_filename
import os
import pandas as pd
import numpy as np
import sklearn
import pickle
import json


#Configs.py

cols=['Cloud Cover Percentage']
model_name="solar_pickle_model.sav"



app= Flask(__name__)

#default page of our web-app
#@app.route('/home')
#def home():
#    return render_template('index.html')

@app.route("/predictions/solar", methods=["GET","POST"])


def solar_pred():

    #reading test data
    data= pd.read_csv('Test_solar.csv')

    X1=data.values

    loaded_model = pickle.load(open(model_name, 'rb'))

    try:

        solar_pred= loaded_model.predict(X1)

    except:

        return jsonify("Error occured while processing your data into our model!")

    print("done")

    response={'data':[],}

    response['data']=list(solar_pred)

    return (response)

#if __name__=='__main__':
#    app.run(debug=False)



# Endpoint for the wind Power predictions
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

    response['data']=list(wind_pred)
    return(response)



#if __name__=='__main__':
#    app.run(debug=True)

#Endpoint for the maintance file upload

app.secret_key = "secret key"

path = os.getcwd()


# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = set(['csv', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == 'filename':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect('/upload')
        else:
            flash('Allowed file types are csv, txt, pdf, png, jpg, jpeg, gif')
            return redirect('/upload')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
