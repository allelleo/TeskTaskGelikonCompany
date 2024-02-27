FROM python:3.6
RUN mkdir /webapp
WORKDIR /webapp
COPY . /webapp
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3", "manage.py", "runserver"]