from fastapi import FastAPI, UploadFile

import ia
import jsonResponseController

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to AReader_AI API"}

@app.post("/")
async def predict(file: UploadFile):
    print(file.content_type)
    if not file.content_type == "image/jpeg":
        return jsonResponseController.returnResponse(-1)
    
    imagefile = await file.read()

    classification = ia.convertToPredict(imagefile)

    return jsonResponseController.returnResponse(classification)

""" import uvicorn
if __name__ == '__main__':
    uvicorn.run("main:app",host='0.0.0.0', port=8080, reload=True) """