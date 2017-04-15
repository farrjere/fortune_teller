from datetime import datetime
from models.models import Model

class Project:
	def __init__(self, 
		id,
		name,
		description = '',
		create_time = datetime.now()):
		assert type(id) is int, 'id must be an integer'
		assert len(name) > 0, 'name must be a non-empty string'
		self.__id = id
		self.__name = name
		self.__description = description
		self.__create_time = create_time
		#publish time should only be set once we have a published model
		#for db restore, thinking of writing a static method that handles that?
		self.__published_time = None
		self.__published_model = None
		self.__models = []

	
	@property
	def id(self):
		return self.__id

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		assert len(name) > 0, 'name must be a non-empty string'
		self.__name = name

	@property
	def description(self):
		return self.__description 

	@description.setter
	def description(self, description):
		self.__description = description

	@property
	def create_time(self):
		return self.__create_time

	@property
	def published_time(self):
		return self.__published_time

	@property
	def models(self):
		return self.__models

	@property
	def published_model(self):
		return self.__published_model

	def add_model(self, model):
		assert type(model) is Model, 'model must be a Model'
		if model not in self.__models:
			self.__models.append(model)

	def publish_model(self, model):
		assert type(model) is Model, 'model must be a Model'
		self.add_model(model)
		self.__published_model = model
		self.__published_time = datetime.now()

	def unpublish_model(self):
		self.__published_model = None
		self.__published_time = None