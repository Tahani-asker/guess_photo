import os
import base64
from flask import Flask, jsonify, request
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route("/")
def home():
    return 'welcome home '

#still uncomplete to test android app 
@app.route("/upload",methods=['POST','GET'])
def predictImage():
    imgb64 = "there is no response"
    if request.method == 'POST':
        imgb64 = request.args.get("imgestr")
        #process imgb64 and return response
    return imgb64







if __name__ == '__main__':
    app.run()



