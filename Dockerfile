FROM python:3.8-alpine

ENV FLASK_APP=app.441D_animal

RUN adduser -D -h /home/animal animal

RUN mkdir /home/animal/curs_SCC_25_animal/ && chown animal:animal /home/animal/curs_SCC_25_animal/

WORKDIR /home/animal/curs_SCC_25_animal/

COPY app app/
COPY dockerstart.sh ./
COPY quickrequirements.txt ./

RUN chmod +x dockerstart.sh

USER animal

RUN python3 -m venv venv
RUN venv/bin/pip install -r quickrequirements.txt

EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
