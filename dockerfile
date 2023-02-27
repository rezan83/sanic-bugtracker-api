
FROM sanicframework/sanic:3.8-latest

WORKDIR /sanic

COPY . .

RUN pipenv install

EXPOSE 8000

CMD ["python", "server.py"]
