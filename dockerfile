# Use a imagem base do Python 3.9
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /code

# Copie o arquivo de requisitos para o diretório de trabalho
COPY ./requirements.txt /code/requirements.txt

# Atualize o pip e instale as dependências do Python
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#install FastAPI tensorflow numpy keras Pillow uvicorn python-multipart

COPY ./model/ /code/model/
COPY ./cloudinaryController.py /code/
COPY ./ia.py /code/
COPY ./jsonResponseController.py /code/
COPY ./note.py /code/
COPY ./font/ /code/font/
COPY ./main.py /code/