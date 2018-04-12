FROM python:2-alpine3.7

COPY requirements.txt .
COPY pdf_writer.py .
COPY templates/ templates/

RUN apk --update add ttf-dejavu fontconfig openjdk8-jre && pip install -r requirements.txt && mkdir -p output

ENTRYPOINT ["python2", "pdf_writer.py"]

