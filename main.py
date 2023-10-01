from io import BytesIO
from fastapi import FastAPI, Form, UploadFile

import ia
import jsonResponseController
import note
import cloudinaryController

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to AReader_AI API"}

@app.post("/")
async def predict(file: UploadFile, text: str = Form(...,max_length=240,media_type="text/plain")):
    if not file.content_type == "image/jpeg":
        return jsonResponseController.returnResponse(-1)
    
    imagefile = await file.read()
    print(text)
    classification = ia.convertToPredict(imagefile)

    if classification <0.5:
        urlImagemAncora = cloudinaryController.uploadImage(imagefile)
        urlImagemNota = cloudinaryController.uploadImage(note.gerarImagem(text))
        print(f" \nclassificação= {classification}\n urlImagemAncora= {urlImagemAncora}\n urlImagemNota= {urlImagemNota}")
    return jsonResponseController.returnResponse(classification)

import uvicorn
if __name__ == '__main__':
    uvicorn.run("main:app",host='0.0.0.0', port=8080, reload=True)