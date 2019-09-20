import json
import redis
from flask import Flask
from abc import ABC, abstractmethod


app = Flask(__name__)


# Python is dynamically typed, so we are creating an interface using an abstract class. 
# Methods defined here must also be defined in subclasses.

class MessageStore(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def write_message(self, message):
        pass

    @abstractmethod
    def word_count(self):
        pass


class RedisMessageStore(MessageStore):

    def __init__(self, host, port, db):
        super().__init__()
        self.host = host
        self.port = port
        self.db = db
        self.r = redis.StrictRedis(host, port, db) # Create our redis server

    def write_message(self, message):
        key = message['id']
        value = message['message']
        if key not in self.r:
            self.r.set(key, value)
            prev_count = int(self.r.get('count'))
            new_count = prev_count + len(value.split())
            self.r.set('count', new_count)

    def word_count(self):
        return int(self.r.get('count'))


class InMemoryMessageStore(MessageStore):

    def __init__(self):
        super().__init__()
        self.m = {}
        self.count = 0

    def write_message(self, message):
        if message['id'] not in self.m:
            self.m[message['id']] = message['message']
            self.count += len(message['message'].split())

    def word_count(self):
        return self.count


r = RedisMessageStore(host='localhost', port=6379, db=0)
r.write_message({"id": "092", "message": "try"}) # Test messages here
r.write_message({"id": "13", "message": "unlucky"})
r.write_message({"id": "099", "message": "add two"})
r.write_message({"id": "584", "message": "very very very long string"})
r.write_message({"id": "099", "message": "add two"})


wc = str(r.word_count()) # Converting to a String
c = 'count = ' + wc # Getting the output formatted


@app.route("/")
def main():
    print(c)
    return json.dumps(c)


if __name__ == "__main__":
    main()










