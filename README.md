## How to use it

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-dashboard-argon.git
$ cd LemarDashboard
$
$ # Virtualenv modules installation (
$ python3 -m venv ./venv
$ . env/Scripts/activate
$
$ # Install modules
$ # SQLIte version
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port 
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

