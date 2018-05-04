#!/usr/bin/env python

from unittest import TestCase

import subprocess
import redis

from socket_io_emitter import Emitter

class TestEmitter(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.redis_server = subprocess.Popen("redis-server", stdout=subprocess.PIPE, shell=True)

    def setUp(self):
        self.opts = dict(host='localhost', port=6379)

    def test_In(self):
        io = Emitter(self.opts)
        io.In('room1')
        self.assertEqual(len(io._rooms), 1)

    def test_To(self):
        io = Emitter(self.opts)
        io.To('room1')
        self.assertEqual(len(io._rooms), 1)

    def test_Of(self):
        io = Emitter(self.opts)
        io.Of('nsp')
        self.assertEqual(io._flags['nsp'], 'nsp')

    def test_Emit(self):
        io = Emitter(self.opts)
        redis_cli = subprocess.Popen('redis-cli monitor', stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)

        output = ''
        while True:
            chunk = redis_cli.stdout.read(1).decode('utf-8')
            if chunk == '' and redis_cli.poll() != None:
                break
            if chunk == '\n':
                io.Emit('broadcast event', 'Hello from socket.io-emitter')
            if chunk != '' and 'PUBLISH' not in output:
                output += chunk
            else:
                redis_cli.kill()
                break

        self.assertTrue('PUBLISH' in output)


    def test_Construct_Emitter_With_Client(self):
        client = redis.StrictRedis(host=self.opts['host'], port=self.opts['port'])
        io = Emitter({'client': client})
        self.assertIsNotNone(io._client)

    def test_Construct_Emitter_With_Options(self):
        io = Emitter(self.opts)
        self.assertIsNotNone(io._client)

    def test_Construct_Emitter_With_Null_Client_And_Null_Options_Raises_Exception(self):
        self.assertRaises(Exception, Emitter, {'client': None})

    @classmethod
    def tearDownClass(cls):
        if not cls.redis_server is None:
            cls.redis_server.kill()
