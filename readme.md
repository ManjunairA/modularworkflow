
Readme before starting project
mlregression2-app

create a file named Dockerfile

add  

FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

then create .gitignore file and add the ignoring files.

then create image
docker build -t <projectName>:<tag> .
For example  docker build -t mlproject:latest .

then if want to see the images created 
docker images

if you want to run the docker image(image id atalst in below command)
docker run -p 5000:5000 -e PORT=5000 07f072d3d5a3 

want to know which docker file is running 
docker ps

want to stop running docker
docker stop container id 

