FROM python:3.9-slim

COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN pip3 install pymysql

WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]