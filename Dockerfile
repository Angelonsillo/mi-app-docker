FROM python:3.9
WORKDIR /app
COPY . .
RUNP pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
