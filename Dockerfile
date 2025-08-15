FROM python:slim-bullseye
RUN pip install flask
WORKDIR /app_assignment
COPY app.py app.py
EXPOSE 8080
CMD ["python3","app.py"]
