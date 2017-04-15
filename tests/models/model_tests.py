from datetime import datetime
from docker.models.images import Image
from docker.errors import ImageNotFound
import json
from models.models import Model
import unittest
from unittest.mock import patch

class ModelTest(unittest.TestCase):

	def test_id(self):
		model = Model(1, 'alpine')
		self.assertEqual(1, model.id)
		def set_id():
			model.id = 2
		self.assertRaises(AttributeError, set_id)

		def create_bad_model():
			model = Model('A bad id', 'alpine')

		self.assertRaises(AssertionError, create_bad_model)


	def test_image(self):
		model = Model(1, 'alpine')
		self.assertEqual('alpine', model.image_name)
		self.assertIsInstance(model.image, Image)
		
		#Check that we get an error when we try to use a non-existant image
		def create_bad_model():
			Model(1, 'notanimage')
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
		model = Model(1, 'alpine', dt)
		self.assertEqual(dt, model.create_time)

		def set_create_time():
			model.create_time = datetime(2018, 1, 1)
		self.assertRaises(AttributeError, set_create_time)		

	def test_input_description(self):
		model = Model(1, 'alpine')
		self.assertEqual(0, len(model.input_desc))

		model.input_desc = {
			'value': 'This value is important for predicting things', 
			'value 2' : 'So is this one'
		}
		self.assertIsInstance(model.input_desc, dict)
		self.assertEqual(2, len(model.input_desc))

	def test_predict(self):
		model = Model(1, 'sk_regression')
		
		with open('example_models/scikit_regression/example_input.json') as input:
			input_val = input.read()

		results = model.predict(input_val)
		self.assertTrue(len(results) > 0)
		self.assertEqual(results, '[[7.3434953766],[7.4932207581],[7.5390592989]]')

if __name__ == '__main__':
    unittest.main()