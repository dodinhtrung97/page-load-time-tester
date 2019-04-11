from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

import time
import simplejson as json
import os
import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class performanceTest:

	def __init__(self, url, log_file, driver_path, loop):
		self.url = url
		self.log_file = log_file
		self.driver_path = driver_path
		self.loop = loop

		self.log_dir = './log'
		self.__options = ''
		self.output_json = {"url": self.url,
						    "averageLoadingTime": 0,
						    "resultSet": []}

		self.load_driver_options()

	def run(self):
		caps = DesiredCapabilities.CHROME
		caps['loggingPrefs'] = {'performance': 'ALL'}

		driver = webdriver.Chrome(desired_capabilities=caps,
								  executable_path=self.driver_path,
								  chrome_options=self.__options)

		attemp_number = 1
		total_loading_time = 0

		while attemp_number <= self.loop:
			# Calculate loading time
			time_start = time.time()
			driver.get(self.url)
			performance_data = driver.execute_script("return window.performance.getEntries();")
			time_end = time.time()

			reduced_performance_data = self.reduce_data_set(performance_data, attemp_number)
			reduced_performance_data['loadingTime'] = (time_end - time_start) * 1000

			# Append current attempt at loading to output data
			total_loading_time += reduced_performance_data['loadingTime']
			self.output_json['resultSet'].append(reduced_performance_data)

			attemp_number += 1	

		self.output_json['averageLoadingTime'] = total_loading_time / self.loop

		if not os.path.exists(self.log_dir):
			os.makedirs(self.log_dir)

		with open(os.path.join(self.log_dir, self.log_file), 'w') as f:
		    json.dump(self.output_json, f)

		driver.close()

	def reduce_data_set(self, data_set, attemp_number):
		"""
		Reduce data set down to only the data that we're interested in
		
		Args:
		    data_set [{}]: Description
		    attemp_number TYPE(int): Current loop
		
		Returns:
		    TYPE: Description
		"""
		result = []

		for data in data_set:
			try:
				result.append({'entryType': data['entryType'],
							   'initiatorType': data['initiatorType'],
							   'loadingTime': data['duration']/2,
							   'name': data['name']})
			except KeyError:
				continue

		loading_time = sum([file['loadingTime'] for file in result])

		return {"loadingTime": 0,
				"attempt_{}".format(attemp_number): result}

	def load_driver_options(self):
		"""
		Load extra options into driver settings
		"""
		self.__options = Options()
		self.__options.add_argument('--headless')
		self.__options.add_argument('--disable-gpu')
		self.__options.add_argument('--no-sandbox')
		self.__options.add_argument('--disable-cache')