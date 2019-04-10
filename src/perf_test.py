from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import simplejson as json
import os
import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class performanceTest:

	def __init__(self, url, log_file, driver_path):
		self.url = url
		self.log_file = log_file
		self.driver_path = driver_path
		self.log_dir = './log'
		self.__options = ''

		self.load_driver_options()

	def run(self):
		caps = DesiredCapabilities.CHROME
		caps['loggingPrefs'] = {'performance': 'ALL'}

		driver = webdriver.Chrome(desired_capabilities=caps,
								  executable_path=self.driver_path,
								  chrome_options=self.__options)

		try:
			driver.get(self.url)
		except Exception as e:
			LOGGER.error("Failed to connect to URL: {}".format(self.url))
			raise

		performance_data = driver.execute_script("return window.performance.getEntries();")
		reduced_performance_data = self.reduce_data_set(performance_data)

		if not os.path.exists(self.log_dir):
			os.makedirs(self.log_dir)

		with open(os.path.join(self.log_dir, self.log_file), 'w') as f:
		    json.dump(reduced_performance_data, f)

		driver.close()

	def reduce_data_set(self, data_set):
		"""
		Reduce data set down to only the data that we're interested in
		
		Args:
		    data_set [{}]: Description
		
		Returns:
		    TYPE: Description
		"""
		result = []

		for data in data_set:
			try:
				result.append({'entryType': data['entryType'],
							   'initiatorType': data['initiatorType'],
							   'loadingTime': data['duration'],
							   'name': data['name']})
			except KeyError:
				continue

		total_loading_time = sum([file['loadingTime'] for file in result])

		return {"url": self.url,
				"loadingTime": total_loading_time,
				"resultSet": result}

	def load_driver_options(self):
		"""
		Load extra options into driver settings
		"""
		self.__options = Options()
		self.__options.add_argument('--headless')
		self.__options.add_argument('--disable-gpu')