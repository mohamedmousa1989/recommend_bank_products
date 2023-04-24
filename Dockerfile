FROM python:3.8-slim-buster

WORKDIR /recommend-bank-products-api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]