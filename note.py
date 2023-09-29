import textwrap
from PIL import Image, ImageFont, ImageDraw
#Limitado a 240 caracteres
textoUmCaractere = "A" #01
textoMuitoCurto = "Exercício de matemática pra segunda" #35
textoCurto = "Aqui o autor lembra-se de sua antiga espada e benevolente fosse alga" #70
textoMedio = "Dada a nota de Velma, nada pode-se fazer pois a mesma está abaixo da média nacional de notas estabelecida pelo governo A " #120
textoLongo = """Se o caminho para o arquivo de fonte estiver correto, verifique se você está usando a função corretamente. A função recebe dois argumentos: o caminho para o arquivo de fonte e o tamanho da fonte. Você pode verificar se está deveras estradaa"""#240

def gerarImagem(texto:str):
    tamanho_fonte_padrao = 100
    tamanho_fonte = tamanho_fonte_padrao/ (len(texto)**0.35)
    fonte = ImageFont.truetype("./font/marker-felt.ttf",tamanho_fonte)
    #fonte = ImageFont.truetype("./font/comic-sans-ms-4.ttf",12)
    imagemReturn = Image.new("RGB", (270,142), color=(255,255,153))

    tamanho_quebra_padrão = 1

    if len(texto) <= 35:
      tamanho_quebra = tamanho_quebra_padrão*((len(texto)**0.8))
    else:
      tamanho_quebra = tamanho_quebra_padrão*((len(texto)**0.68))
    
    texto_quebrado = textwrap.wrap(text=texto,width=tamanho_quebra) #formula para tamanho quebra
                                                        #120C = 30
                                                        #240C = 40
                                                        # 70C = 28
    
    caneta = ImageDraw.Draw(imagemReturn)
 

    print(f"tamanho da fonte: {tamanho_fonte} \n e tamanho texto: {tamanho_quebra}")

    valorY=3 #formula para valor
    if len(texto) <= 50:
        multiplyValorY = 30
    else:
       multiplyValorY = 20


    for linha in texto_quebrado:
        caneta.text((10,valorY),text=linha,fill="white",font=fonte,stroke_width=1,stroke_fill="black")
        valorY+=multiplyValorY

    return imagemReturn

gerarImagem(textoUmCaractere).show()
gerarImagem(textoMuitoCurto).show()
gerarImagem(textoCurto).show()
gerarImagem(textoMedio).show()
gerarImagem(textoLongo).show()



""" for i in range(1,100):
    print(f"valor i {i} //" + "fator:"+ str(i/100))
    print( "70c - " + str(1*(70**(i/100))))
    print( "120c - " + str(1*(120**(i/100))))
    print( "240c - " + str(1*(240**(i/100)))) """