FROM python:3.11-alpine
WORKDIR /betsapp
COPY ./betsapp /betsapp
COPY ./requirements.txt /betsapp
RUN pip install -r requirements.txt
EXPOSE 3000
CMD ["gunicorn","--bind=0.0.0.0","bets:app"]