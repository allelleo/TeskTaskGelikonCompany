FROM python:3.10-slim-buster
RUN mkdir /webapp
WORKDIR /webapp
COPY ./requirements.txt /webapp/requirements.txt
RUN apt-get update && apt-get install -y git gcc\
    && pip install -r requirements.txt
COPY . /webapp
EXPOSE 8000
CMD ["python3", "manage.py", "runserver"]