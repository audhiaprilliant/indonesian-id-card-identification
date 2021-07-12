FROM python:3.6-slim-buster
MAINTAINER Audhi Aprilliant
RUN apt-get update -y && apt-get install -y libmariadb3 libmariadb-dev
EXPOSE 80
EXPOSE 5000
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]