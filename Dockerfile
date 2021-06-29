FROM python:3
WORKDIR /docker_roll
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python","roll.py"]