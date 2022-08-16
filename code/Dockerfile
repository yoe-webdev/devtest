FROM python:3.6

EXPOSE 5000

WORKDIR /code

COPY requirements.txt /code 

RUN pip install -r requirements.txt

COPY templates /code/templates
COPY static /code/static
COPY app.py /code

CMD python app.py