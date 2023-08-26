FROM python:3.7
RUN pip install fastapi uvicorn pydantic
COPY ./app /app
WORKDIR /app
CMD ["uvicorn","api:app","--host","0.0.0.0","--port","8000"]




