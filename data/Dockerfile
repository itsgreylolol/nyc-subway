FROM python:3.11-slim-buster

WORKDIR /code/data

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "-m", "main" ]
