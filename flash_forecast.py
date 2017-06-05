from sanic import Sanic
from sanic.response import text
import os
import asyncio
import uvloop
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Project, Model

app = Sanic(__name__)
app.config.from_pyfile('config.py')

connection = ''

@app.listener('before_server_start')
async def setup_db(app, loop):
	from models.models import Project, Model
	app.engine = create_engine(app.config.DATABASE_CONNECTION, echo=True)
	Base = declarative_base()
	Base.metadata.create_all(app.engine)
	app.Session = sessionmaker(bind=app.engine)

@app.route('/')
async def root(request):
	return text('Welcome to Flash Forecast')

@app.route('/projects')
async def projects(request):
	session = app.Session()
	projects = []
	for project in session.query(Project):
		projects.append(project)
	return json({"projects": projects})

@app.route('/projects/<id:int>')
async def project(request, id):
	pass

@app.route('/projects', methods=['POST'])
async def create_project(request):
	pass


@app.route('/projects/<id:int>', methods=['PUT'])
async def update_project(request, id):
	pass

@app.route('/projects/<id:int>', methods=['DELETE'])
async def delete_project(request, id):
	pass

@app.route('/projects/<id:int>/predict', methods=['POST'])
async def predict(request, id):
	pass

@app.route('/projects/<id:int>/models')
async def models(request):
	pass

@app.route('/projects/<project_id:int>/models/<id:int>')
async def model(request, project_id, id):
	pass

@app.route('/projects/<project_id:int>/models/', methods=['POST'])
async def create_model(request, project_id):
	pass

@app.route('/projects/<project_id:int>/models/<id:int>', methods=['PUT'])
async def update_model(request, project_id, id):
	pass

@app.route('/projects/<project_id:int>/models/<id:int>', methods=['DELETE'])
async def delete_model(request, project_id, id):
	pass

@app.route('/projects/<project_id:int>/models/<id:int>/publish', methods=['PUT'])
async def publish_model(request, project_id, id):
	pass

@app.route('/projects/<project_id:int>/models/<id:int>/unpublish', methods=['PUT'])
async def unpublish_model(request, project_id, id):
	pass

app.run(host="0.0.0.0", port=8000, debug=True)