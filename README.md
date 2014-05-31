socket.io-python-emitter
========================

A Python implementation of socket.io-emitter

`socket.io-python-emitter` allows you to communicate with socket.io servers
easily from Python processes.

## How to use

```py
  io=Emitter({'host': 'localhost', 'port':6379})
  io.Emit('broadcast event','Hello from socket.io-python-emitter')
        
```

###Open Source Projects in Use
* [redis-py](https://github.com/andymccurdy/redis-py) by Andy McCurdy @andymccurdy
* [msgpack-python](https://github.com/msgpack/msgpack-python) by MessagePack
