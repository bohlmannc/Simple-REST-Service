# Simple-REST-Service
REST service to count words in a JSON message

Necessary dowloads:

-Redis

-Flask

To build the project:
First, download Python 3.4 or greater (3.7 was used). Python will come with the json and abc modules without any additional downloads.

Once you have Python, you can use pip commands to install a virtual env, Flask, and Redis.

In the command line: 

```
python3 -m pip install virtualenv
pip3 install Flask
pip3 install redis
```

Then create a new folder for this project:

```
mkdir myproject
cd myproject
```

And activate the virtualenv:

```
python3 -m venv venv
.venv/bin/activate
```

Download rest_service.py and save it to your project folder.

Now, you need to download and start the redis server (http://download.redis.io).

Navigate to the redis folder after downloading:

```
cd
cd Downloads
cd redis-5.0.5/
cd src
```

Now you are in the redis source file. Use the following commands to install and test redis:

```
make install
make test
```

And one final command to start the server:

```./redis-server```

Now, it's time to launch the Flask server.

```
export FLASK_APP=rest_service.py
python -m flask run
```

You will be able to see the current count at: http://127.0.0.1:5000/.
You can add messages by editing rest_service.py. For example:

```
r.write_message({"id": "0121", "message":"goodbye world"})
```

Run the script again in python, return to the command line, export the file, and run flask again. Your count should go up.

Possible Improvements

Even for a problem as simple as this, we could make things interesting: What will the requests/sec be for ```word_count``` and ```write_message```?

If messages are relatively short and ```word_count``` does a lot more traffic than ```write_message```, then you should 100% count the words in the message in write_message and update the count along with writing the message to the store.

If messages are regularly insanely long and ```write_message``` does a lot  of traffic relative to ```word_count```, then you have a couple options:

-If you're okay with returning stale word_count to the client, then you could only write the message in ```write_message```, and then have another thread that polls the store for messages whose words havent been counted yet and counts them and updates the count.

-When ```write_message``` is called you write it to store, but you also write it to an in memory store as well. In this way, when ```word_count``` is called it will go the store to read the current count, and then it will also go to that in memory store and proceed to count all the words there and add them to get the final count, clear everything in the in memory store, write the new count to the store, and then return the count.

Best solution:
If ```write_message``` sees a message of size > some threshold of bytes, then it hands it off to another thread to perform the count and update it in the store. Otherwise, it just does the count right then and there and updates it and writes the message in the store.
