FROM python:3.9.0

RUN apt-get update

RUN echo "testing"

WORKDIR /home/

RUN git clone https://github.com/hyun98/Docker_Practice.git

WORKDIR /home/Docker_Practice/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000"]
