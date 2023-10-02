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
    urlImage = await asyncio.to_thread(cloudinaryController.uploadImage, imagefile)
    return urlImage

async def get_url_note_text(text):
    urlNote = await asyncio.to_thread(cloudinaryController.uploadImage, note.gerarImagem(text))
    return urlNote

@app.post("/")
async def predict(file: UploadFile, text: str = Form(...,max_length=240,media_type="text/plain")):
    if not file.content_type == "image/jpeg":
        return jsonResponseController.notAcceptable()
    
    imagefile = await file.read()

    classification_task = asyncio.create_task(get_classification(imagefile))

    classification = await classification_task


    if classification <0.5:
        url_image_task = asyncio.create_task(get_url_image(imagefile))
        url_note_task = asyncio.create_task(get_url_note_text(text))
        urlImage = await url_image_task
        urlNote = await url_note_task
        print(f" \nclassificação= {classification}\n urlImagemAncora= {urlImage}\n urlImagemNota= {urlNote}")
        return jsonResponseController.ok(classification,urlImage,urlNote)
    else:
        return jsonResponseController.badRequest(classification)

import uvicorn
if __name__ == '__main__':
    uvicorn.run("main:app",host='0.0.0.0', port=8080, reload=True)