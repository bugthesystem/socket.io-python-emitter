import threading

from emitter. import Emitter


__author__ = 'ziyasal'


class AppWorker:
    def __init__(self):
        self.interval = 6000 * 1

    def start(self):
        io = Emitter(dict(host='localhost',port=6379))
        io.Emit('broadcast event', 'Hello from socket.io-emitter')
        threading.Timer(self.interval, self.start).start()

if __name__ == '__main__':
    app = AppWorker()
    app.start()
