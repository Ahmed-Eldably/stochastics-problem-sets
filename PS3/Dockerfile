FROM python:3.5.10-slim-buster
RUN apt-get update


WORKDIR /app
COPY ./ ./
RUN pip install --upgrade pip
#RUN pip install -r requirements.txt

CMD ["python3", "ps3.py"]