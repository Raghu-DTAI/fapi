FROM python:3.10

WORKDIR /frontend




RUN pip install fastapi
RUN pip install streamlit
RUN pip install requests

EXPOSE 8501

COPY . /frontend


ENTRYPOINT ["streamlit", "run", "strcal.py", "--server.port=8501", "--server.address=0.0.0.0"]