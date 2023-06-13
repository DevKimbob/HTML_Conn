FROM python:3.7-alpine

WORKDIR /code

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80

ENV CUSTOM_HEADER='Connection Check'
ENV BG_COLOR=white
ENV FONT_COLOR=black

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN apk add --no-cache curl

EXPOSE 80
COPY build/ .

CMD ["flask", "run"]
