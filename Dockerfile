FROM python:3.11-bullseye

RUN pip install pandas matplotlib

COPY iris.csv /app/iris.csv

COPY iris_demo.py /app/iris_demo.py

WORKDIR /app

RUN python iris_demo.py