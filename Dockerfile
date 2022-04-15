FROM python:3.9-slim-buster
WORKDIR /app
EXPOSE 5000
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./app .
ENV FLASK_ENV=development
CMD [ "flask", "run", "--host", "0.0.0.0" ]
