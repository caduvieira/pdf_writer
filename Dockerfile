FROM python:2-alpine3.7

COPY requirements.txt .
RUN apk --update add ttf-dejavu fontconfig openjdk8-jre && pip install -r requirements.txt && mkdir -p output

COPY pdf_writer.py .
COPY templates/ templates/

ENTRYPOINT ["python2", "pdf_writer.py"]

