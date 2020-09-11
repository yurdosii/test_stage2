# Stage 2 - test task

## Clone repository
```
git clone https://github.com/yurdosii/test_stage2.git
```

## Check code quality
Run [flake8](https://flake8.pycqa.org/en/latest/)
```
flake8 src/
```
Run [black](https://github.com/psf/black)
```
black src/
```
Install and run [pyright](https://github.com/microsoft/pyright)
```
sudo npm install -g pyright

pyright src/
```

## Set environment variables
Add .env file
```
cd src/news_api
touch .env
nano .env
```
Inside of file you can set variables:
* "DEBUG" (optional, default=False)
* "DATABASE_URL" (optional, docker-compose override this variable)
* "SECRET_KEY"

Filled file will look like:
```
DEBUG=<value>
DATABASE_URL=<value>
SECRET_KEY=<value>
```

## Run API
Run using docker-compose
```
docker-compose build

docker-compose up
```
Run migrations if you run API for the first time (run in another terminal):
```
docker-compose run --rm web ./src/manage.py migrate
```

## Additional links
Postman collection - https://www.getpostman.com/collections/9aa6b713d9be24efa6fa

Deployment link (on Heroku) - [link](http://test-stage2.herokuapp.com/posts/)
