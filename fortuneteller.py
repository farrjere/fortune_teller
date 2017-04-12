from sanic import Sanic
from sanic.response import text
from sanic.response import json
import rpy2.robjects as robjects

app = Sanic(__name__)

@app.route("/eval/R", methods=['POST'])
async def evaluate_R(request):
    r_to_run = request.json['r']
    results = robjects.r(r_to_run)
    return json(results)

@app.route('/')
async def root(request):
	return text('Welcome to Fortuneteller')

app.run(host="0.0.0.0", port=8000, debug=True)