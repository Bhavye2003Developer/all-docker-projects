FROM ubuntu

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get install -y python3

RUN apt-get install -y g++

COPY pythonFile.py /usr/share

CMD ["python3", "/usr/share/pythonFile.py"]