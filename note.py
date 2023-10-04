import textwrap
from PIL import Image, ImageFont, ImageDraw, ImageOps
from io import BytesIO

#Limitado a 240 caracteres
def calculateFontSize(lenText: int):
   max_size = 100 # Define o tamanho máximo da Fonte
   factor = 0.35 # Alterar de acordo com o tamanho mínimo da fonte para X caracteres
   return max_size/(lenText**factor) # Ex: max_Caracteres = 240 -> tamanho_max = 100; tamanho_min = 15; fator = 0.35; -> Com 240c teremos o tamanho da fonte = 14,68676 e com 1c = 100

def calculateBreakTextValue(lenTexto:int):
   break_value_min = 1
   if lenTexto <= 15:
    return break_value_min*lenTexto   
   elif lenTexto<= 35:
    return break_value_min*(lenTexto**0.9)
   elif lenTexto<= 70:
    return break_value_min*(lenTexto**0.79)
   elif lenTexto<= 120:
    return break_value_min*(lenTexto**0.75)
   else:
    return break_value_min*(lenTexto**0.68)

def breakText(text:str):
    break_size = round(calculateBreakTextValue(len(text))) 
    return textwrap.wrap(text=text,width=break_size,break_long_words=True)

def calculateDistanceBetweenLines(lenTexto:int):
    if lenTexto <= 50:
        return 30
    elif lenTexto <= 100:
        return 25
    else:
        return 20

def generateImage(text:str):
    text_size = len(text)

    font = ImageFont.truetype("./font/marker-felt.ttf",calculateFontSize(text_size))

    bkImage = Image.new("RGB", (270,142), color=(255,255,153)) 

    pen = ImageDraw.Draw(bkImage)

    text_broken = breakText(text)

    valueY=3
    valueYMultiply = calculateDistanceBetweenLines(text_size)

    for line in text_broken:
        pen.text((10,valueY),text=line,fill="black",font=font,stroke_width=0,stroke_fill="black")
        valueY+=valueYMultiply

    bkImage = ImageOps.expand(bkImage,border=1,fill="black")

    image_bytes = BytesIO()
    bkImage.save(image_bytes, format='JPEG')
    image_bytes = image_bytes.getvalue()
    return image_bytes