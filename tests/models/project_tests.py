from datetime import datetime
from docker.models.images import Image
from docker.errors import ImageNotFound
import json
import models
from models.models import Project
from models.models import Model

import unittest
from unittest.mock import patch


class ProjectTest(unittest.TestCase):
    def test_id(self):
        id = 1
        project = Project(_id = id, _name='Movie Predictions')
        self.assertEqual(1, project.id)

        def set_id():
            project.id = 2
        self.assertRaises(AttributeError, set_id)

        def bad_project():
            Project(_id='Bad Moon', _name='Rising')
        self.assertRaises(AssertionError, bad_project)

    def test_name(self):
        name = 'Movie Predictions'
        project = Project(_id = 1, _name='Movie Predictions')
        self.assertEqual(name, project.name)
        name = 'New Name'
        project.name = name
        self.assertEqual(name, project.name)

        def bad_name():
            project = Project(_id = id, _name='')
        self.assertRaises(AssertionError, bad_name)

    def test_description(self):
        descrpition = 'This is a project for producing IMDB rating predictions for movies'
        project = Project(_id = 1, _name='Movie Predictions', _description=descrpition)
        self.assertEqual(project.description, descrpition)
        project.description = 'Better desc'
        self.assertEqual('Better desc', project.description)

    def test_create_time(self):
        dt = datetime(2017, 3, 1)
        project = Project(_id=1, _name='Movie Predictions', _create_time=dt)
        self.assertEqual(dt, project.create_time)

        def set_create_time():
            project.create_time = datetime(2018, 1, 1)
        self.assertRaises(AttributeError, set_create_time)

    def test_publish_time(self):
        project = Project(_id = 1, _name='Movie Predictions')

        def set_published_time():
            project.published_time = datetime(2017, 1, 1)

        self.assertEqual(None, project.published_time)
        self.assertRaises(AttributeError, set_published_time)

    def test_add_model(self):
        model = Model(_id=1, _image_name='alpine')
        project = Project(_id = 1, _name='Alpine Slopes')

        self.assertEqual([], project.models)
        project.add_model(model)

        self.assertEqual([model], project.models)

        project.add_model(model)
        self.assertEqual([model], project.models)

        def add_non_model():
            project.add_model(1)

        self.assertRaises(AssertionError, add_non_model)

    def test_publish_model(self):
        model = Model(_id=1, _image_name='alpine')
        project = Project(_id = 1, _name='Alpine Slopes')
        self.assertEqual(None, project.published_model)
        self.assertEqual([], project.models)
        self.assertEqual(None, project.published_time)

        project.publish_model(model)
        self.assertEqual(model, project.published_model)
        self.assertEqual([model], project.models)
        first_time = project.published_time
        self.assertTrue(first_time is not None)

        new_model = Model(_id=2, _image_name='alpine')
        project.publish_model(new_model)
        self.assertEqual(2, len(project.models))
        self.assertEqual(new_model, project.published_model)
        self.assertTrue(first_time != project.published_time)

        project.publish_model(model)
        self.assertEqual(2, len(project.models))
        self.assertEqual(model, project.published_model)

        def publish_non_model():
            project.publish_model(1)

        self.assertRaises(AssertionError, publish_non_model)

    def test_unpublish_model(self):
        model = Model(_id=1, _image_name='alpine')
        project = Project(_id=1, _name='Alpine Slopes')
        self.assertEqual(None, project.published_model)
        self.assertEqual([], project.models)
        project.publish_model(model)
        self.assertEqual(model, project.published_model)

        project.unpublish_model()
        self.assertEqual(None, project.published_model)
        pass

    def test_rollback_model(self):
        pass

    def test_models(self):
        pass


if __name__ == '__main__':
    unittest.main()
