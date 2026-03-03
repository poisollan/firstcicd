FROM python:3.11-slim

WORKDIR /app

#copy requirements and install packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy your app
COPY myapp2.py .

EXPOSE 5000

CMD ["python", "myapp2.py"]
