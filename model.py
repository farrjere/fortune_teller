import docker

class Model:
	def __init__(self, 
		name, 
		image,
		version = 1.0):
		self.__name = name
		self.__version = version
		self.__client = docker.from_env()
		self.__image = self.__client.images.get(image)
		pass

	@property
	def image(self):
		return self.__image

	@property
	def name(self):
		return self.__name

	@property
	def version(self):
		return self.__version

	@version.setter
	def version(self, version):
		if version >= self.__version:
			self.__version = version