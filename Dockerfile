FROM python:3.10

ADD main.py .

RUN pip install pygame

CMD ["python","./main.py"]
