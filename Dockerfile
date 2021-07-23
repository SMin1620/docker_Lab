FROM python:3.9.0

# RUN apt-get update

# RUN apt-get install -y python3.9

# RUN apt-get install -y git

# RUN apt-get update

# RUN apt-get upgrade -y pip

RUN echo "testing"

WORKDIR /home/

RUN git clone https://github.com/hyun98/Docker_Practice.git

WORKDIR /home/Docker_Practice/

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
