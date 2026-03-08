## Parse Nginx Exercise

In this exercise, a custom container based on nginx **1.29** is used, to which the following files are added: _index.html, index.png, and structure.png_ to a directory called _cwd_ that hangs from the nginx home directory.

This container listens on port _8080_ and also mounts the nginx logs directory to a local directory called _nginx-logs_.

A Python 3 script is included to parse the _access.log_ file, as described in the exercise. This script does not use any special libraries.

> How to use: python3 parser.py ./nginx-logs/access.log

Tested with Python 3.9.x and Python 3.13.x
