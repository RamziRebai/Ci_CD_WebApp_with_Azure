FROM python:3.7-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
        rm requirements.txt
COPY ./app /app
CMD ["uvicorn", "app.main:app"]
