FROM python:3.10

EXPOSE 3000

WORKDIR /app

COPY requirements.txt /app
COPY templates /app/templates

RUN pip install -r requirements.txt --upgrade pip
RUN pip install flask-mysql
RUN pip install pandas
RUN pip install geopy

COPY . /app

CMD python app.py