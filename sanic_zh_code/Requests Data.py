from sanic.response import json
from sanic import Sanic
app = Sanic()
@app.route("/json")
def post_json(request):
    return json({ "received": True, "message": request.json })
@app.route("/query_string")
def query_string(request):
    return json({ "parsed": True, "args": request.args, "url": request.url, "query_string": request.query_string })
@app.route("/files")
def post_json(request):
    test_file = request.files.get('test')

    file_parameters = {
        'body': test_file.body,
        'name': test_file.name,
        'type': test_file.type,
    }

    return json({ "received": True, "file_names": request.files.keys(), "test_file_parameters": file_parameters })

from sanic.response import json
from sanic import Blueprint

bp = Blueprint('my_blueprint')

@bp.route('/')
async def bp_root(request):
    if request.app.config['DEBUG']:
        return json({'status': 'debug'})
    else:
        return json({'status': 'production'})