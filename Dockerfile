FROM python:3

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
RUN rm requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/app"
COPY ./app /app
