__author__ = 'ziyasal'

import redis
import msgpack


class Emitter:
    EVENT = 2
    BINARY_EVENT = 5

    def __init__(self, opts):
        self.opts = opts
        self._rooms = []
        self._flags = {}
        self.redis = self._client(self.opts['host'], self.opts['port'])

        if not 'key' in self.opts:
            self.key = 'socket.io#emitter'
        else:
            self.key = self.options.key + '#emitter'

    #Limit emission to a certain `room`.
    def In(self, room):
        if not room in self.rooms:
            self._rooms.extend(room)

    #Limit emission to a certain `room`.
    def To(self, room):
        return self.In(room)

    #Limit emission to certain `namespace`.
    def Of(self, nsp):
        self._flags['nsp'] = nsp
        return self

    #Send the packet.
    def Emit(self, *args):
        arguments = locals().keys()
        packet = {}
        extras={}

        packet['data'] = args
        packet['type'] = self.BINARY_EVENT if self._hasBin(args) else self.EVENT


        # set namespace to packet
        if 'nsp' in self._flags:
            packet['nsp'] = self._flags.nsp
            del self._flags['nsp']

        extras['flags']=self._flags if len(self._flags) > 0 else ''
        extras['rooms']=self._rooms if len(self._rooms) > 0 else ''


        self.redis.publish(self.key, msgpack.packb([packet, extras]))

        self._flags = {}
        self._rooms = []


    #Not implemented yet
    def _hasBin(self,param):
        return False

    #Create a redis client from a `host:port` uri string.
    def _client(self, host, port):
        if host is None:
            raise Exception('Missing redis `host`')
        if port is None:
            raise Exception('Missing redis `port`')

        return redis.StrictRedis(host=host, port=port)