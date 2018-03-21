__author__ = 'ziyasal'

from setuptools import setup

setup(
    name='socket.io-emitter',
    version='0.1.4',
    author='Ziya SARIKAYA',
    author_email='sarikayaziya@gmail.com',
    packages=['emitter'],
    url='https://github.com/ziyasal/socket.io-python-emitter',
    license='LICENSE',
    description='A Python implementation of socket.io-emitter',
    install_requires=['msgpack-python', 'redis'],
    include_package_data=True
)
