from sanic.exceptions import ServerError

@app.route('/killme')
def i_am_ready_to_die(request):
    raise ServerError("Something bad happened", status_code=500)

from sanic.exceptions import abort
from sanic.response import text

@app.route('/youshallnotpass')
def no_no(request):
        abort(401)
        # this won't happen
        text("OK")

from sanic.response import text
from sanic.exceptions import NotFound

@app.exception(NotFound)
def ignore_404s(request, exception):
    return text("Yep, I totally found the page: {}".format(request.url))