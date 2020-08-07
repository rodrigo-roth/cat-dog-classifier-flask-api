from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from modules.preprocess_image_cl import PreprocessImage
from modules.db_connection import SQLConnection
from keras.preprocessing import image
from flask import request
from PIL import Image
import numpy as np
import sqlite3
import base64
import keras
import flask
import time
import io

app = flask.Flask(__name__)

app.config["DEBUG"] = True 

@app.route("/predict64", methods=["POST"])
def predict():
    """
    Retorna a predição de uma imagem codificada em base64 enviada via API;
    
    A imagem é enviada codificada em base64 através do método POST junto com o nome do usuário, 
    é então armazenada no banco de dacos "classifier.db" a predição da imagem, 
    o nome do usuário e o timestamp em que foi enviada, e no fim retorna a predição da imagem.       
    """
    
    payload = request.get_json(force=True)
    user = payload['user']
    encoded = payload['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = PreprocessImage().preprocess_image(image, target_size=(64, 64))
    model2 = load_model("./model.h5")
    result = model2.predict(processed_image).tolist()

    if result[0][0] == 1:
        prediction = 'dog'
    else:
        prediction = 'cat'
    
    timestamp = time.time()

    SQLConnection("classifier.db").insert_data(user, timestamp, prediction)

    return prediction

if __name__ == '__main__':
    
    app.run()
