FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./src ./src


CMD ["uvicorn", "src.main:app", "--host", "localhost", "--port", "8000"]
