# Register Blueprints/Views.
from .users import UserController
from .upload import upload
from application.extensions import jinja

def init_views(app):
    app.add_route(UserController.as_view(), '/api/user')
    import application.controllers.pages
    import application.controllers.api
    
    app.blueprint(upload)
    @app.route('/')
    def index(request):
        return jinja.render('index.html', request)
    
    