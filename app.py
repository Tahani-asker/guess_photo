import os
import base64
from flask import Flask, jsonify, request
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route("/")
def home():
    return 'welcome home '


@app.route("/upload",methods=['POST','GET'])
def predictImage():
    imgb64 = "there is no response"
    if request.method == 'POST':
        imgb64 = request.args.get("imgestr")
    return imgb64







if __name__ == '__main__':
    app.run()



