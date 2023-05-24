FROM python:3.9
EXPOSE 8080
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

COPY app /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "uvicorn", "app:app", "--port", "8080", "--host", "0.0.0.0",  "--log-level", "debug"]