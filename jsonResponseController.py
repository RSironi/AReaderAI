from fastapi.responses import JSONResponse

def notAcceptable():
    return JSONResponse(content={"message": "O arquivo file precisa ser image/jpeg"}, status_code=406)
def ok(value:int, urlAncora:str,urlAnotacao:str):
    return JSONResponse(content={"message": "valid","classification": str(value), "urlAnchor":urlAncora,"urlAnnotation":urlAnotacao}, status_code=200)
def badRequest(value:int):
    return JSONResponse(content={"message": "invalid","classification": str(value)}, status_code=400)