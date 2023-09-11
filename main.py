from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
#import uvicorn
from io import BytesIO

from PIL import Image

import numpy
import tensorflow as tf

from keras.applications.mobilenet_v3 import preprocess_input

app = FastAPI(title="areader AI api")
model = tf.keras.models.load_model("model/model4")

@app.post('/')
async def predict(file: UploadFile):
    if not file.filename.lower().endswith(('.jpg', '.jpeg')):
        return JSONResponse(content={"message": "Apenas arquivos de imagem .jpg são permitidos"}, status_code=406)
    
    imagefile = await file.read()

    image = numpy.empty((1, 224, 224, 3))
    image_pil = Image.open(BytesIO(imagefile))
    image_pil = image_pil.resize([224, 224])
    image[0] = image_pil

    image = preprocess_input(image)
    classification = model.predict(image)
    classification = classification[0][0] #converte [[valor]] para valor
    print(classification)

    if classification < 0.5:
        return JSONResponse(content={"message": "valid","classification": str(classification)}, status_code=200)
    else:
        return JSONResponse(content={"message": "invalid","classification": str(classification)}, status_code=400)

#if __name__ == '__main__':
    #uvicorn.run('main:app', host='0.0.0.0', port=8000)