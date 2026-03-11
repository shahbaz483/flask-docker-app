FROM python:3.13.1

WORKDIR C:\Users\shahb\OneDrive\Desktop\Python

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]