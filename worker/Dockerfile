FROM python:3.9-slim
# THIS LINE IS THE FIX FOR BLANK LOGS:
ENV PYTHONUNBUFFERED=1 
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]