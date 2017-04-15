import docker
import datetime
from types import *
class Model:
	def __init__(self, 
		id, 
		image, 
		create_time = datetime.datetime.now(),
		input_desc = {},
		commands = []):
		assert type(id) is int, 'id must be an integer'
		self.__id = id
		self.__client = docker.from_env()
		self.__image_name = image
		self.__image = self.__client.images.get(image)
		self.__create_time = create_time
		self.__input_desc = input_desc

	@property
	def image(self):
		return self.__image

	@property
	def image_name(self):
		return self.__image_name

	@property
	def id(self):
		return self.__id

	@property
	def create_time(self):
		return self.__create_time

	@property 
	def input_desc(self):
		return self.__input_desc

	@input_desc.setter
	def input_desc(self, input_desc):
		if len(input_desc) > 0:
			self.__input_desc = input_desc

	def predict(self, pred_input):
		results = self.__client.containers.run(self.__image_name, [pred_input], remove=True)
		results = results.decode('UTF-8')
		return results
