FROM python:3

WORKDIR /

COPY . .

RUN apt-get -y update
RUN pip3 install flask

EXPOSE 5001

CMD ["python3", "./app.py"]
