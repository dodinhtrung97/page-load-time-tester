from perf_test import performanceTest
import argparse
import logging

LOGGER = logging.getLogger(__name__)

def main():
	parser = argparse.ArgumentParser(description='Page loading performance test')
	parser.add_argument('chromedriver', metavar='DRIVER', type=str, help='Relative path to chromedriver')
	parser.add_argument('url', metavar='URL', type=str, help='URL of page to do performance test')
	parser.add_argument('log', metavar="LOG", type=str, help='Name of output json log file')

	args = parser.parse_args()

	performance_test = performanceTest(driver_path=args.chromedriver,
									   url=args.url, 
									   log_file=args.log)
	performance_test.run()

if __name__ == '__main__':
	main()