# Simple project with Django, DRF and VueJS

## Back-end setup

### Setup virtual environment and install required dependencies
```
python3 -m venv env
source/env/bin/activate

pip install -r requirements.txt
```

### Export list of variables below in terminal with values related to local database configuration
```
SECRET_KEY=secret_key
ALLOWED_HOSTS=*

NAME=test_name
USER=test_user
PASSWORD=test_password
HOST=0.0.0.0
PORT=5433
```

### Apply migrations and run server
```
python manage.py migrate
python manage.py runserver
```

### Load initial data to fill local database
```
cd backend/scripts/
./load-initial-data.sh
```

---

## Front-end setup

### Install packages
```
yarn install
```

### Compile and run frontend with hot-reloads for development
```
yarn run serve
```

### Note: export variable node_options to avoid openssl error in case if you are using node version 16+
```
export NODE_OPTIONS=--openssl-legacy-provider
```
