socket.io-python-emitter
========================

A Python implementation of `socket.io-emitter <https://github.com/automattic/socket.io-emitter>`_.

`socket.io <http://socket.io/>`_ provides a hook point to easily allow you to emit events to browsers from anywhere so `socket.io-python-emitter` communicates with `socket.io <http://socket.io/>`_ servers through redis.

We made some changes, compatible socket.io-redis 0.2.0 and socket.io 0.1.4.

How to use
----------

**Install via pip**
  
  pip install socket.io-emitter

.. code-block:: python

  import emitter from Emitter
  io=Emitter({'host': 'localhost', 'port':6379})
  io.Emit('broadcast event','Hello from socket.io-python-emitter')

API
---

Emitter(opts)
-------------

The following options are allowed:

- `client`: is a `redis-py <https://github.com/andymccurdy/redis-py>`_ compatible client
   This argument is optional.
- `key`: the name of the key to pub/sub events on as prefix (`socket.io`)
- `host`: host to connect to redis on (`localhost`)
- `port`: port to connect to redis on (`6379`)

If you don't want to supply a redis client object, and want
`socket.io-python-emitter` to initialize one for you, make sure to supply the
`host` and `port` options.

Specifies a specific `room` that you want to emit to.

Emitter#In(room):Emitter
------------------------

.. code-black:: python

  io=Emitter({'host': 'localhost', 'port':6379})
  io.In("room-name").Emit("news","Hello from python emitter");

Emitter#To(room):Emitter
------------------------

.. code-black:: python

 io=Emitter({'host': 'localhost', 'port':6379})
    
 io.To("room-name").Emit("news","Hello from python emitter");

We are flattening the room parameter from [] and *argv, so you can also send to several rooms like this (both examples are valid):

.. code-black:: python

 io=Emitter({'host': 'localhost', 'port':6379})

 io.To(["room1", "room2"]).Emit("news","Hello from python emitter");
 io.To("room1", "room2").Emit("news","Hello from python emitter");

Emitter#Of(namespace):Emitter
-----------------------------

Specifies a specific namespace that you want to emit to.

.. code-black:: python

 io=Emitter({'host': 'localhost', 'port':6379})
    
 io.Of("/nsp").In("room-name").Emit("news","Hello from python emitter");

License
-------

MIT License

Copyright (c) 2014 Ziya SARIKAYA

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Open Source Projects in Use
---------------------------

* `redis-py <https://github.com/andymccurdy/redis-py>`_ by Andy McCurdy @andymccurdy
* `msgpack-python <https://github.com/msgpack/msgpack-python>`_ by MessagePack

z i λ a s a l.
