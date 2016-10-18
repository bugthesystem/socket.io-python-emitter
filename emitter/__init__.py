__author__ = 'ziyasal'
__version__ = '0.1.3'

import redis
import msgpack


class Emitter:
    EVENT = 2
    BINARY_EVENT = 5

    def __init__(self, opts):
        self._opts = opts
        self._rooms = []
        self._flags = {}

        self.uid = "emitter"

        if 'client' in self._opts and self._opts['client'] is not None:
            self._client = self._opts['client']
        else:
            self._client = self._createClient()

        self._key = self._opts.get("key", 'socket.io')

    # Limit emission to a certain `room`.
    def In(self, *room):
        self._rooms.append(room)
        return self

    # Limit emission to a certain `room`.
    def To(self, *room):
        return self.In(room)

    # Limit emission to certain `namespace`.
    def Of(self, nsp):
        self._flags['nsp'] = nsp
        return self

    # Send the packet.
    def Emit(self, *args):
        packet = {}
        extras = {}

        packet['data'] = args
        packet['type'] = self.BINARY_EVENT if self._hasBin(args) else self.EVENT


        # set namespace to packet
        if 'nsp' in self._flags:
            packet['nsp'] = self._flags['nsp']
            del self._flags['nsp']
        else:
            packet['nsp'] = '/'

        extras['flags'] = self._flags if len(self._flags) > 0 else ''

        rooms = self._getRooms()
        extras['rooms'] = rooms if len(rooms) > 0 else ''

        if extras['rooms']:
            for room in rooms:
                chn = "#".join((self._key, packet['nsp'], room, ""))
                self._client.publish(chn, msgpack.packb([self.uid,packet, extras]))
        else:
            chn = "#".join((self._key, packet['nsp'], ""))
            self._client.publish(chn, msgpack.packb([self.uid,packet, extras]))

        self._flags = {}
        self._rooms = []

    # Makes [[1,2],3,[4,[5,6]]] into an iterator of [1,2,3,4,5,6]
    def _flatten(self, root):
      if isinstance(root, (list, tuple)):
        for element in root:
          for e in self._flatten(element):
            yield e
      else:
        yield root

    # Get a list of unique rooms
    def _getRooms(self):
      return list(set(self._flatten(self._rooms)))

    # Not implemented yet
    def _hasBin(self, param):
        return False

    # Create a redis client from a `host:port` uri string.
    def _createClient(self):
        if not 'host' in self._opts:
            raise Exception('Missing redis `host`')
        if not 'port' in self._opts:
            raise Exception('Missing redis `port`')

        kwargs = {
            'host': self._opts['host'],
            'port': self._opts['port'],
        }

        if 'password' in self._opts:
            kwargs['password'] = self._opts['password']

        return redis.StrictRedis(**kwargs)
