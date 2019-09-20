# Simple-REST-Service
REST service to count words in a JSON message

Necessary dowloads:
-Redis
-Flask

To build the project:
First, download Python (3.4 or greater - 3.7 was used). Python will come with the json and abc modules without any additional downloads.

Once you have Python, you can use pip commands to install a virtual env, Flask, and Redis.

In the command line: 

```python3 -m pip install virtualenv```
```pip3 install Flask```
```pip3 install redis```

Then create a new folder for this project:

```mkdir myproject```
```cd myproject```

And activate the virtualenv:

```python3 -m venv venv```
```.venv/bin/activate```

Download rest_service.py and save it to your project folder.

Now, you need to download and start the redis server (http://download.redis.io).

Navigate to the redis folder after downloading:

```cd redis-5.0.5/```
```cd src```

Now you are in the redis source file. Use the following commands to install and test redis:

```make install```
```make test```

And one final command to start the server:

```./redis-server```

Now, it's time to launch the Flask server.

```export FLASK_APP=rest_service.py```
```python -m flask run```

Future improvements to the rest service:
