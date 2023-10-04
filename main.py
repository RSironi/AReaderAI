from fastapi import FastAPI, Form, UploadFile
import asyncio

import ia
import jsonResponseController
import note
import cloudinaryController

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to AReader_AI API"}

async def get_classification(imagefile):
    classification = await asyncio.to_thread(ia.convertToPredict, imagefile)
    return classification

async def get_url_image(imagefile):
    url_image = await asyncio.to_thread(cloudinaryController.uploadImage, imagefile)
    return url_image

async def get_url_note_text(text):
    url_note = await asyncio.to_thread(cloudinaryController.uploadImage, note.generateImage(text))
    return url_note

@app.post("/")
async def predict(file: UploadFile, text: str = Form(...,max_length=240,media_type="text/plain")):
    if not file.content_type == "image/jpeg":
        return jsonResponseController.notAcceptable()
    
    image_file = await file.read()

    classification_task = asyncio.create_task(get_classification(image_file))

    classification = await classification_task

    if classification <0.5:
        url_image_task = asyncio.create_task(get_url_image(image_file))
        url_note_task = asyncio.create_task(get_url_note_text(text))
        url_image = await url_image_task
        url_note = await url_note_task
        print(f" \nclassificação= {classification}\n urlImagemAncora= {url_image}\n urlImagemNota= {url_note}")
        return jsonResponseController.ok(classification,url_image,url_note)
    else:
        return jsonResponseController.badRequest(classification)

""" import uvicorn
if __name__ == '__main__':
    uvicorn.run("main:app",host='0.0.0.0', port=8080, reload=True) """