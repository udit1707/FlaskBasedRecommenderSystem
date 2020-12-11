from flask import Flask, jsonify, request, render_template, redirect, url_for,send_file 
from flask_api import FlaskAPI, status, exceptions
from PIL import Image
from werkzeug.utils import secure_filename
# from flaskext.mysql import MySQL
import os, json 
import requests 
import threading
import csv
import Model
app = Flask(__name__)
  

# handle=''
#repeatedly calls node endpoint to update csv dataset
# def callToCSV():
#     global handle
#     resp=requests.get('http://localhost:3000/treks/trekToCSV') 
#     jsonDa=json.loads(resp.text)
#     print(jsonDa)
#     dict_data=jsonDa["treks"]
#     csv_columns = ['id','name','image','mean_rating','count_ratings']
#     csv_file = "dataset/model.csv"
#     try:
#         with open(csv_file, 'w') as csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#             writer.writeheader()
#             for data in dict_data:
#                 writer.writerow(data)  
#         files = {'fileUpload': ('model.csv', open('dataset/model.csv', 'rb')),}      
#         resp = requests.post('https://www.filestackapi.com/api/store/S3?key=AH01fkwUHQAKj8lTQIinFz', files=files)
#         handle=json.loads(resp.text)["url"][33:]
#         print("URL")
#         print(handle)
#         print("File Created!")
#         os.remove("dataset/model.csv")
#     except IOError:
#         print("I/O error")
#     threading.Timer(20.0, callToCSV).start()

@app.route('/') 
def index(): 
	return "Flask server" 

@app.route('/fetchTop5', methods = ['POST']) 
def recommen():
    result=Model.recommenFetch()
    result=json.dumps(result)
    print(result)    
    return jsonify({'msg': 'success','data_result':result})

# threading.Timer(20.0, callToCSV).start()


if __name__ == "__main__": 
	app.run(threaded=True, port = int(os.environ.get('PORT', 5000)))
