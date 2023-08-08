FROM python:3.7-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
        rm requirements.txt
EXPOSE 8000
COPY ./app /app
CMD ["uvicorn", "main:app", "--port", "8000"]
