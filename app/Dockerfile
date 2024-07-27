FROM python:3.10

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]

# building image:
    # docker build -t amandawillrich/pe-iii:latest .

# running image:
    # docker run -d --rm -p 8000:8000 amandawillrich/pe-iii

# running local development:
    # docker run -d --rm -p 8000:8000 -v $(pwd):/usr/src/app amandawillrich/pe-iii
    ## or using docker-compose.yml