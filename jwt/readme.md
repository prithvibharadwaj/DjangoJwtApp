# djangoJwtApp

Django Rest API with jwt authentication

## Installation

First, clone the repo, and follow the below commands to start

```bash
cd djangoJwtApp/jwt
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate the virtual environment

```bash
source venv/bin/activate
```
Install all the packages from req.txt file

```bash
pip3 install req.txt
```

Migrate

```bash
python3 manage.py migrate
```

Start the app
```bash
python3 manage.py runserver
```

## Testing

Install the postman on the system and use the follwing to url to signin and signup

choose post in postman and under body use raw and select JSON
to signup use:
```bash
http://127.0.0.1:8000/api/signup
```

to signin use:
```bash
http://127.0.0.1:8000/api/signin
```

```json
{
 "email":"ghi@gmail.com",
 "password":"123456"
}
```