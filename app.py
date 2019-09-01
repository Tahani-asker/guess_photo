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




def readphoto(imgstring):
    imgdata = base64.b64decode(imgstring)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)




if __name__ == '__main__':
    app.run()



