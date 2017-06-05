import docker
from datetime import datetime
from types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB

TAG_LENGTH = 128 #https://docs.docker.com/engine/reference/commandline/tag/#usage
Base = declarative_base()

class Project(Base):
	__tablename__ = 'projects'
	_id = Column('id', Integer, primary_key=True)
	_name = Column('name', String(128), nullable=False)
	_description = Column('description', String(), nullable=False)#Go to the max!
	_create_time = Column('create_time', DateTime, default=datetime.now)

	def __init__(self, **kwargs):
		super(Project, self).__init__(**kwargs)
		assert type(self._id) is int, 'id must be an integer'
		assert len(self._name) > 0, 'name must be a non-empty string'
		if self._create_time is None:
			self._create_time = datetime.now()
	
	@hybrid_property
	def id(self):
		return self._id

	@hybrid_property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		assert len(name) > 0, 'name must be a non-empty string'
		self._name = name

	@hybrid_property
	def description(self):
		return self._description 

	@description.setter
	def description(self, description):
		self._description = description

	@hybrid_property
	def create_time(self):
		return self._create_time

	@hybrid_property
	def models(self):
		return self._models

	@property
	def published_model(self):
		published_models = [model for model in self._models if model.published]
		if len(published_models) == 1:
			return published_models[0]
		elif len(published_models) > 1:
			raise AttributeError('Can only have one published model at a time')
		else:
			return None#This means that the project has not published a model yet

	def add_model(self, model):
		assert type(model) is Model, 'model must be a Model'
		if model not in self._models:
			self._models.append(model)

class Model(Base):
	__tablename__ = 'models'
	_id = Column('id', Integer, primary_key=True)
	_image_name = Column('image_name', String(TAG_LENGTH), nullable=False)
	_project_id = Column('project', Integer, ForeignKey('projects.id'), nullable=False)
	_project = relationship(Project, backref="_models", primaryjoin='_project_id=Project._id')
	_create_time = Column('create_time', DateTime, default=datetime.now)
	_input_desc = Column('input_desciption', String())
	_published = Column('published', sqlalchemy.types.Boolean, default=False, nullable=False)
	_published_time = Column('published_time', DateTime, nullable=True)

	def __init__(self, **kwargs):
		super(Model, self).__init__(**kwargs)
		assert type(self._id) is int, 'id must be an integer'
		#assert type(project) is Project, 'project must be a valid Project'
		if self._input_desc == None:
			self._input_desc = {}
		if self._create_time == None:
			self._create_time = datetime.now()
		self._client = docker.from_env()
		self._image = self._client.images.get(self.image_name)

	@property
	def image(self):
		return self._image

	@hybrid_property
	def image_name(self):
		return self._image_name

	@hybrid_property
	def id(self):
		return self._id

	@hybrid_property
	def create_time(self):
		return self._create_time

	@hybrid_property 
	def input_desc(self):
		return self._input_desc

	@input_desc.setter
	def input_desc(self, input_desc):
		if len(input_desc) > 0:
			self._input_desc = input_desc

	@hybrid_property
	def project(self):
		return self._project

	def publish(self):
		self.publish(datetime.now())

	def publish(self, publish_time):
		for model in self._project._models:
			model._published = False
			model._published_time = None

		self.published = True
		self._published_time = publish_time

	def predict(self, pred_input):
		if self._published:
			results = self._client.containers.run(self.image_name, [pred_input], remove=True)
			results = results.decode('UTF-8')
			return results
		else:
			return 'Model is not published, please publish to make predictions'