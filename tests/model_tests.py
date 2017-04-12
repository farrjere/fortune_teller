import unittest
import sys 
sys.path.append('..')
from model import Model
from docker.models.images import Image
from docker.errors import ImageNotFound
class ModelTest(unittest.TestCase):

	def test_name(self):
		name = 'Magic Model'
		model = Model(name, 'alpine')
		self.assertEqual(name, model.name)
		def set_name():
			model.name = 'Another Name'
		self.assertRaises(AttributeError, set_name)

	def test_version(self):
		model = Model('model', 'alpine', 0.5)
		self.assertEqual(model.version, 0.5)
		model.version = 0.6
		self.assertEqual(model.version, 0.6)
		model.version = 0.5
		self.assertEqual(model.version, 0.6)

	def test_image(self):
		model = Model('Model', 'alpine')
		self.assertIsInstance(model.image, Image)
		def create_bad_model():
			Model('Model', 'notanimage')
		self.assertRaises(ImageNotFound, create_bad_model)

if __name__ == '__main__':
    unittest.main()