import sys

__author__ = 'ziyasal'

from unittest import TestCase
from emitter import Emitter
import subprocess
import redis


class TestEmitter(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.redis_server = subprocess.Popen("redis-server", stdout=subprocess.PIPE, shell=True)

    def setUp(self):
        self.opts = dict(host='localhost', port=6379)

    def test_In(self):
        self.fail()

    def test_To(self):
        self.fail()

    def test_Of(self):
        self.fail()

    def test_Emit(self):
        io = Emitter(self.opts)
        redis_cli = subprocess.Popen("redis-cli monitor", stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)

        output = ""
        while True:
            out = redis_cli.stdout.read(1)
            if out == '' and redis_cli.poll() != None:
                break
            if out == '\n':
                io.Emit('broadcast event', 'Hello from socket.io-emitter')
            if out != '' and 'PUBLISH' not in output:
                output += out
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