FROM python:3.6-alpine
RUN mkdir /app
COPY . /app
RUN touch /app/.env
RUN pip install --find-links /app/wheels -r /app/requirements.txt
RUN pip install gunicorn
WORKDIR /app
EXPOSE 5000
CMD ["./boot.sh"]
