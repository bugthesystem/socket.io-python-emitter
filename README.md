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

## API

### Emitter(opts)

The following options are allowed:

- `client`: is a [redis-py](https://github.com/andymccurdy/redis-py) compatible client
   This argument is optional.
- `key`: the name of the key to pub/sub events on as prefix (`socket.io`)
- `host`: host to connect to redis on (`localhost`)
- `port`: port to connect to redis on (`6379`)

If you don't want to supply a redis client object, and want
`socket.io-python-emitter` to initialize one for you, make sure to supply the
`host` and `port` options.

Specifies a specific `room` that you want to emit to.

### Emitter#In(room):Emitter
```py

  io=Emitter({'host': 'localhost', 'port':6379})
  io.In("room-name").Emit("news","Hello from python emitter");
```
### Emitter#To(room):Emitter
```py

 io=Emitter({'host': 'localhost', 'port':6379})
    
 io.To("room-name").Emit("news","Hello from python emitter");
```

### Emitter#Of(namespace):Emitter
Specifies a specific namespace that you want to emit to.
```py

 io=Emitter({'host': 'localhost', 'port':6379})
    
 io.Of("/nsp").In("room-name").Emit("news","Hello from python emitter");
```


## License

MIT

###Open Source Projects in Use
* [redis-py](https://github.com/andymccurdy/redis-py) by Andy McCurdy @andymccurdy
* [msgpack-python](https://github.com/msgpack/msgpack-python) by MessagePack
