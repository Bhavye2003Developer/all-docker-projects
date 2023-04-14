FROM ubuntu

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get install -y python3 && apt-get install -y python3-django

RUN apt-get install -y net-tools

COPY learningDocker /usr/share/

CMD ["python3", "/usr/share/manage.py" ,"runserver", "0.0.0.0:8000"]
