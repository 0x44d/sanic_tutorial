from sanic import Sanic
from sanic import response
app = Sanic()

@app.route('/text')
def handle_request(request):
    return response.text('Hello world!')

@app.route('/json')
def handle_request(request):
    return response.json({'message': 'Hello world!'})
@app.route('/file')
async def handle_request(request):
    return await response.file('/root/Downloads/0')
@app.route("/streaming")
async def index(request):
    async def streaming_fn(response):
        response.write('foo')
        response.write('bar')
    return response.stream(streaming_fn, content_type='text/plain')
@app.route('/big_file.png')
async def handle_request(request):
    return await response.file_stream('/srv/www/whatever.png')


@app.route('/redirect')
def handle_request(request):
    return response.redirect('/json')

@app.route('/raw')
def handle_request(request):
    return response.raw('raw data')
@app.route('/json1')
def handle_request(request):
    return response.json(
        {'message': 'Hello world!'},
        headers={'X-Served-By': 'sanic'},
        status=200
    )

if __name__=="__main__":
    app.run(debug=True)