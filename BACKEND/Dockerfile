FROM python:3.7
RUN pip install fastapi uvicorn pydantic
COPY ./app /app
CMD ["uvicorn","app.api:app","--host","0.0.0.0","--port","15400"]




