# Stage 2 - test task

## Clone repository
```
git clone https://github.com/yurdosii/test_stage2.git
```

## Set environment variables
Add .env file:
```
cd test_stage2/src/news_api
touch .env
nano .env
```
Inside of the file set DEBUG and SECRET_KEY variables:
```
DEBUG=True
SECRET_KEY=<value>  (e.g. "SECRET_KEY=10randomkey15")
```

## Run API
Run using docker-compose:
```
docker-compose build

docker-compose up
```
Run migrations if you run API for the first time (run in another terminal):
```
docker-compose run --rm web ./src/manage.py migrate
```

## Check code quality
In order to check code quality you should create virtual environment (you should be in 'test-stage2' folder):
```
virtualenv venv
```
Activate environment:
```
source venv/bin/activate
```
Install requirements:
```
pip install -r requirements.txt
```
Now you can run [flake8](https://flake8.pycqa.org/en/latest/):
```
flake8 src/
```
Run [black](https://github.com/psf/black):
```
black src/
```
Install and run [pyright](https://github.com/microsoft/pyright):
```
sudo npm install -g pyright

pyright src/
```

## Additional links
Postman collection - https://www.getpostman.com/collections/9aa6b713d9be24efa6fa

Deployment link (on Heroku) - [link](http://test-stage2.herokuapp.com/posts/)
