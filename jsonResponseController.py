from fastapi.responses import JSONResponse

def returnResponse(value: float):

    if value == -1:
       return JSONResponse(content={"message": "O arquivo file precisa ser image/jpeg"}, status_code=406)
    elif value == -2:
       return JSONResponse(content={"message": "O text precisa ser um text/plain"}, status_code=406)
    elif value < 0.5:
        return JSONResponse(content={"message": "valid","classification": str(value)}, status_code=200)
    else:
        return JSONResponse(content={"message": "invalid","classification": str(value)}, status_code=400)