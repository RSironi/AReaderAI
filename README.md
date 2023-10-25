# AReaderAI

API da IA desenvolvida para o TCC do projeto AReader (visualização em realidade aumentada de anotações virtuais em livros). 

IA classifica se uma foto é de uma página de livro ou não.

Recebe um HTTP Post contendo uma imagem e um texto, se aprovado a imagem ele transforma o texto em uma 'anotação.jpeg' e envia ao CDN, se toda a operação for um sucesso ele retorna a URL de ambas as imagens.

- Utiliza
  - FastAPI (melhor performance, como objetivo é retornar apenas json)
  - Funções Assincronas
  - Handler básico de Reposta e Erros
  - Validação de imagem e texto
  - Tamanho da anotação responsivo limitado a 240 caracretes.
  - Docker
  - CDN Cloudinary
  - Uvicorn (servidor web ASGI, para Python, útil para rodar IA com APIs)

## Instalação
Recomenda-se editar as configurações com suas próprias credenciais e acessos.

Via docker
```yml
#execute o dockerfile
docker build -t areaderAI .
```
Via python
```bash
#execute o pip
pip install -r requirements.txt
```

## Uso
Via docker
```yml
#execute a imagem docker gerada após o build
#porta default da imagem utilizada -> port = 80
docker run -p 80:80 IMAGE
```
Via python
```bash
#Descomente o uvicorn run no fim do código
#execute o arquivo main
python main.py
```
