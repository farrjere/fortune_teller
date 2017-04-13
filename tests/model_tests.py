from datetime import datetime
from docker.models.images import Image
from docker.errors import ImageNotFound

import sys 
sys.path.append('..')
from model import Model

import unittest
from unittest.mock import patch

class ModelTest(unittest.TestCase):

	def test_id(self):
		id = 1
		model = Model(1, 'alpine')
		self.assertEqual(1, model.id)
		def set_name():
			model.id = 2
		self.assertRaises(AttributeError, set_name)

	def test_image(self):
		model = Model('Model', 'alpine')
		self.assertEqual('alpine', model.image_name)
		self.assertIsInstance(model.image, Image)
		
		#Check that we get an error when we try to use a non-existant image
		def create_bad_model():
			Model('Model', 'notanimage')
		self.assertRaises(ImageNotFound, create_bad_model)

		#Validate that image_name is read only
		def set_image_name():
			model.image_name = 'another_image'
		self.assertRaises(AttributeError, set_image_name)

		#Validate that we are read only with the image
		def set_image():
			model.image = None
		self.assertRaises(AttributeError, set_image)

	def test_create_time(self):
		#Need to fix this so that patching dates is correct
		# with patch('model.datetime') as mock_dt:
		# 	dt = datetime(2017, 1, 1)
		# 	mock_dt.datetime.now.return_value = dt
		# 	mock_dt.side_effect = lambda *args, **kw: datetime(*args, **kw)
		# 	model = Model('Model', 'alpine')
		# 	self.assertEqual(dt, model.create_time)

		dt = datetime(2017, 3, 1)
		model = Model('Model', 'alpine', dt)
		self.assertEqual(dt, model.create_time)

		def set_create_time():
			model.create_time = datetime(2018, 1, 1)
		self.assertRaises(AttributeError, set_create_time)		

	def test_input_description(self):
		model = Model('Model', 'alpine')
		self.assertEqual(0, len(model.input_desc))

		model.input_desc = {
			'value': 'This value is important for predicting things', 
			'value 2' : 'So is this one'
		}
		self.assertIsInstance(model.input_desc, dict)
		self.assertEqual(2, len(model.input_desc))

	def test_commands(self):
		pass

if __name__ == '__main__':
    unittest.main()