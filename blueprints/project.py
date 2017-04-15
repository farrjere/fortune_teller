from sanic.blueprints import Blueprint
from sanic.response import json
from sanic_openapi import doc

blueprint = Blueprint('Project', '/project')
