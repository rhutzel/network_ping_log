#!python
#cython: language_level=3

from datetime import datetime
import logging
from logging.handlers import RotatingFileHandler
import os
import sys
import time


def prepare_logger() -> logging.Logger:
	logger = logging.getLogger('network_ping_log')
	logger.setLevel(logging.INFO)

	try:
		os.mkdir('./logs')
	except FileExistsError:
		pass

	handler = RotatingFileHandler('./logs/ping_log.csv', backupCount=50, maxBytes=1024000)
	logger.addHandler(handler)
	return logger


def is_ping_successful(host) -> bool:
	return True if os.system("ping -c 1 {}".format(host)) == 0 else False


def main(host):
	logger = prepare_logger()
	while True:
		time.sleep(10)
		ping_result = is_ping_successful(host)
		logger.info('{},{}'.format(datetime.now().isoformat(), str(ping_result)))


if __name__ == "__main__":
	last_arg = sys.argv[-1]
	if len(sys.argv) != 2 or last_arg == "--help":
		print("\nUsage: ./bin/network_ping_log hostname\n")
		sys.exit(0)
	print("Monitoring [{}] ...".format(last_arg))
	try:
		main(last_arg)
	except KeyboardInterrupt:
		print("\nStopped monitoring.")
		sys.exit(0)
