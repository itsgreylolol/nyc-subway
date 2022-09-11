FROM 3.10.6-slim-buster:latest

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "-m", "main" ]
