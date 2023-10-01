from io import BytesIO
import numpy
import tensorflow as tf

from PIL import Image

from keras.applications.mobilenet_v3 import preprocess_input


model = tf.keras.models.load_model("./model")

def convertToPredict(byteImage: BytesIO):

    image = numpy.empty((1,224,224,3))

    image_pil = Image.open(BytesIO(byteImage))
    image_pil= image_pil.resize([224,224])
    image[0] = image_pil
    image = preprocess_input(image)
    classification = model.predict(image)
    classification = classification[0][0]

    return classification