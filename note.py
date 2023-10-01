import textwrap
from PIL import Image, ImageFont, ImageDraw, ImageOps
from io import BytesIO

#Limitado a 240 caracteres
def CalculoTamanhoFonte(lenTexto: int):
   tamanho_maximo = 100 # Define o tamanho máximo da Fonte
   fator = 0.35 # Alterar de acordo com o tamanho mínimo da fonte para X caracteres
   return tamanho_maximo/(lenTexto**fator) # Ex: max_Caracteres = 240 -> tamanho_max = 100; tamanho_min = 15; fator = 0.35; -> Com 240c teremos o tamanho da fonte = 14,68676 e com 1c = 100

def CalculoQuebraTexto(lenTexto:int):
   quebra_min = 1
   if lenTexto <= 15:
    return quebra_min*lenTexto   
   elif lenTexto<= 35:
    return quebra_min*(lenTexto**0.9)
   elif lenTexto<= 70:
    return quebra_min*(lenTexto**0.79)
   elif lenTexto<= 120:
    return quebra_min*(lenTexto**0.75)
   else:
    return quebra_min*(lenTexto**0.68)

def quebrarTexto(texto:str):
    tamanho_quebra = round(CalculoQuebraTexto(len(texto))) 
    return textwrap.wrap(text=texto,width=tamanho_quebra,break_long_words=True)

def CalculoDistanciaEntreLinhas(lenTexto:int):
    if lenTexto <= 50:
        return 30
    elif lenTexto <= 100:
        return 25
    else:
        return 20

def gerarImagem(texto:str):
    tamanhoTexto = len(texto)

    fonte = ImageFont.truetype("./font/marker-felt.ttf",CalculoTamanhoFonte(tamanhoTexto))

    imagemReturn = Image.new("RGB", (270,142), color=(255,255,153)) 

    caneta = ImageDraw.Draw(imagemReturn)

    texto_quebrado = quebrarTexto(texto)

    valorY=3
    multiplicadorValorY = CalculoDistanciaEntreLinhas(tamanhoTexto)

    for linha in texto_quebrado:
        caneta.text((10,valorY),text=linha,fill="black",font=fonte,stroke_width=0,stroke_fill="black")
        valorY+=multiplicadorValorY

    imagemReturn = ImageOps.expand(imagemReturn,border=1,fill="black")

    image_bytes = BytesIO()
    imagemReturn.save(image_bytes, format='JPEG')
    image_bytes = image_bytes.getvalue()
    return image_bytes