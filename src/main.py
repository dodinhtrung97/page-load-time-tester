from perf_test import performanceTest
import argparse
import logging
import os

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():
	parser = argparse.ArgumentParser(description='Page loading performance test')
	parser.add_argument('chromedriver', metavar='DRIVER', type=str, help='Relative path to chromedriver')
	parser.add_argument('url', metavar='URL', type=str, help='URL of page to do performance test')
	parser.add_argument('log', metavar="LOG", type=str, help='Name of output json log file')
	parser.add_argument('--loop', default=1, type=int, help='Number of times to reload page')

	args = parser.parse_args()

	if not os.path.isfile(args.chromedriver):
		raise FileNotFoundError('Failed to access browser driver at designated path {}'.format(args.chromedriver))

	performance_test = performanceTest(driver_path=args.chromedriver,
									   url=args.url, 
									   log_file=args.log,
									   loop=args.loop)
	performance_test.run()

if __name__ == '__main__':
	main()