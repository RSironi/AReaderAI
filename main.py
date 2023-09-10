from flask import Flask, request, Response
from PIL import Image

import numpy
import tensorflow as tf

from keras.applications.mobilenet_v3 import preprocess_input

app = Flask(__name__)
model = tf.keras.models.load_model("model/model4")

@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']

    image = numpy.empty((1, 224, 224, 3))
    image_pil = Image.open(imagefile)
    image_pil = image_pil.resize([224, 224])
    image[0] = image_pil

    image = preprocess_input(image)
    classification = model.predict(image)
    classification = classification[0][0] #converte [[valor]] para valor
    print(classification)

    if classification < 0.5:
        return Response(status=200)
    else:
        return Response(status=400)

if __name__ == '__main__':
    from waitress import serve
    serve(app,port=8080, host = "0.0.0.0")