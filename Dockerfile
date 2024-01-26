FROM python:3

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt
# RUN pip install -U python-dotenv
# RUN pip install eventlet

COPY . .