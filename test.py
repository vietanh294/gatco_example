from sanic import Sanic
from sanic.response import json, text
from sanic import Blueprint
from sanic.views import HTTPMethodView

app = Sanic()

methods=['GET', 'POST', 'DELETE', 'PUT']
methods = frozenset((m.upper() for m in methods))
        # sets of methods used for different types of endpoints
no_instance_methods = methods & frozenset(('GET', ))

bp = Blueprint('my_blueprint', url_prefix='/api/v1')
async def bp_root(request, name):
    return json({'my': name})

class SimpleAsyncView(HTTPMethodView):
    async def get(self, request, name):
        return text('I am async get method: ' + name)

#app.add_route(SimpleAsyncView.as_view(), '/')

#print(no_instance_methods)
bp.add_route(bp_root,'/user/<name>',methods=no_instance_methods)

bp.add_route(SimpleAsyncView.as_view(),'/user1/<name>',methods=no_instance_methods)

app.blueprint(bp)

@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)