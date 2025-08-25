from flask import Blueprint
from .routes import a

user = Blueprint(
    'user',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/user/static'
)

# Registro interno de rutas
'/user/ Prefijo usuario'
user.register_blueprint(a.aUser) # /user/

