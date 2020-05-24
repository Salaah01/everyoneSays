"""Listens for changes in the Redis database and on changes dispatches actions
to update the postGreSQL database.
"""

from datetime import date
import time
import redis
import psycopg2


class Worker:

    def __init__(self):
        self.currDate = date.today()
        self._redisConn = self._set_redis_connection()
        self._listener = self._set_listener('vote')

    @staticmethod
    def _set_redis_connection():
        """Sets the redis connection."""
        return redis.Redis(host='redis', port=6379, db=0)

    def _set_listener(self, key):
        """Sets an object to listen for changes for `key` in the redis db."""
        listener = self.get_redis_connection().pubsub()
        listener.psubscribe(key)
        return listener

    def incrementVotes(self):
        """Increments the daily votes."""
        self.get_redis_connection().incr('votesToday')        

    def resetVotes(self):
        """Resets the daily votes."""
        self.get_redis_connection().set('votesToday', 0)

    def get_redis_connection(self):
        """Gets the redis connection."""
        return self._redisConn

    def get_listener(self):
        """Returns the redis listener."""
        return self._listener

    def dispatcher(self):
        """Listens for changes in the redis db and dispatches actions
        accordingly.
        """
        while True:
            msg = self.get_listener().get_message()
            if msg:
                print(msg['data'])
                self.incrementVotes()
            else:
                time.sleep(0.1)
            
            if self.currDate != date.today():
                self.resetVotes()
                self.currDate = date.today()

if __name__ == "__main__":
    Worker().dispatcher()
