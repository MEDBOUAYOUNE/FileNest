FROM python:3.11

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

# CMD ["./wait-for-it.sh", "python", "manage.py", "runserver", "0.0.0.0:8000"]