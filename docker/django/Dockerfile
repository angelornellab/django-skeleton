FROM python:3.11.2-alpine

RUN mkdir /application
WORKDIR /application

COPY . /application/

RUN pip install -r docker/django/requirements.txt

CMD ["gunicorn", "-c", "docker/django/gunicorn.conf.py", "--bind", ":8000", "--chdir", "core", "core.wsgi:application"]
