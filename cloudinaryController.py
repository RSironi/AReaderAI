from io import BytesIO
import cloudinary

import cloudinary.uploader
import cloudinary.api

## Enviar imagem ao Cloudinary 
def uploadImage(file):
    upload = cloudinary.uploader.upload(file)
    return upload["secure_url"]

def uploadBytesImage(image_bytes):

    response = cloudinary.uploader.upload_image(image_bytes)

    # Retorne o URL da imagem
    return response["secure_url"]


cloudinary.config(
    cloud_name = "dj4pzc33p",
    api_key = "459697167742439",
    api_secret = "h1Vbikvt57dEJ2P5AzzSxq9r_lo",
    secure = True
)

#print(uploadImage("antest/teste.jpg"))