from sanic import Sanic
from sanic.response import text
from sanic.response import json
import rpy2.robjects as robjects

app = Sanic(__name__)

@app.route('/')
async def root(request):
	return text('Welcome to Flash Forecast')

app.run(host="0.0.0.0", port=8000, debug=True)