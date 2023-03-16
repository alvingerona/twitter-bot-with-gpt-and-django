# Twitter Bot with GPT and Django
The goal of this project is to use GPT completion API to generate tweets, which will then be stored in a database. Django is used to manage these tweets, and users will have the ability to validate which tweets can be automatically posted.

To use this system, you will need to have a Twitter developer account and access to the consumer key, consumer secret, access token, and access secret in order to post tweets. Additionally, an OpenAI key will be required in order to generate the tweets themselves.

This require pipenv - https://github.com/pypa/pipenv

### pipenv Shell
```
$ pipenv shell
```

### install package
```
pipenv install [PACKAGE]
```

### How to start the project?
Run the command
```
docker compose up -d --build
```

### On the very first running of the app on the server
Create super admin user, do exec to tweeterbot_app and run the command:
```
python manage.py createsuperuser
```

This will ask for username and password of the super admin user.

### Access website
http://localhost:8012/