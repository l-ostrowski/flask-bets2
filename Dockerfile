FROM python:3.11-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 3000
CMD ["gunicorn","--bind=0.0.0.0","wsgi:app"]