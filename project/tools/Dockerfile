FROM python:3.8

ENV port 8000

WORKDIR /work_dir

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
RUN apt-get -q update && apt-get -qy install netcat

#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

EXPOSE $port
