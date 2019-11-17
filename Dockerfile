FROM python:3.7-slim-buster

RUN apt-get update
RUN apt-get install -y jq gcc node-less

RUN pip --no-cache-dir install gunicorn[gevent]

RUN useradd saport

WORKDIR /home/saport

COPY Pipfile.lock .
#RUN pipenv lock -r > requirements.txt
RUN jq -r '.default | to_entries[] | .key + .value.version ' Pipfile.lock > requirements.txt

RUN pip --no-cache-dir install --default-timeout=100 --no-cache-dir -r requirements.txt

RUN apt-get purge -y jq gcc

COPY .env config.py manage.py ./
COPY app app/
COPY migrations migrations/
RUN chown -R saport:saport ./
USER saport

EXPOSE 5000
#RUN python manage.py db migrate
RUN python manage.py db upgrade
CMD ["gunicorn", "-b", \
        ":5000", \
        "-k", "gevent", \
        "-w", "2", \
        "--access-logfile", "-", \
        "manage:app"]
