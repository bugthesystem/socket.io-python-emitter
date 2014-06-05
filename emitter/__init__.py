__author__ = 'ziyasal'
__version__ = '0.1.0'

import redis
import msgpack


class Emitter:
    EVENT = 2
    BINARY_EVENT = 5

    def __init__(self, opts):
        self._opts = opts
        self._rooms = []
        self._flags = {}

        if 'client' in self._opts and self._opts['client'] is not None:
            self._client = self._opts['client']
        else:
            self._client = self._createClient()

        if not 'key' in self._opts:
            self.key = 'socket.io#emitter'
        else:
            self.key = self.options.key + '#emitter'

    # Limit emission to a certain `room`.
    def In(self, room):
        if not room in self.rooms:
            self._rooms.extend(room)

    # Limit emission to a certain `room`.
    def To(self, room):
        return self.In(room)

    #Limit emission to certain `namespace`.
    def Of(self, nsp):
        self._flags['nsp'] = nsp
        return self

    #Send the packet.
    def Emit(self, *args):
        packet = {}
        extras = {}

        packet['data'] = args
        packet['type'] = self.BINARY_EVENT if self._hasBin(args) else self.EVENT


        # set namespace to packet
        if 'nsp' in self._flags:
            packet['nsp'] = self._flags.nsp
            del self._flags['nsp']

        extras['flags'] = self._flags if len(self._flags) > 0 else ''
        extras['rooms'] = self._rooms if len(self._rooms) > 0 else ''

        self._client.publish(self.key, msgpack.packb([packet, extras]))

        self._flags = {}
        self._rooms = []


    #Not implemented yet
    def _hasBin(self, param):
        return False

    #Create a redis client from a `host:port` uri string.
    def _createClient(self):
        if not 'host' in self._opts:
            raise Exception('Missing redis `host`')
        if not 'port' in self._opts:
            raise Exception('Missing redis `port`')

        return redis.StrictRedis(host=self._opts['host'], port=self._opts['port'])