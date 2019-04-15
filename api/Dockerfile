FROM python:3.6-jessie
RUN apt update
COPY . /app
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /app
ENV PORT 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
