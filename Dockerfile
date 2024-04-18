FROM python:slim

WORKDIR /app

RUN apt update -y
RUN apt install pkg-config python3-dev default-libmysqlclient-dev build-essential -y

COPY requirements.txt .

RUN export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
RUN export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`
RUN pip install -r requirements.txt --break-system-packages

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

