from flask import Blueprint
from .routes import a, b

auth = Blueprint(
    'auth', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/auth/static'
    )

# Registro interno de rutas
auth.register_blueprint(a.aLogin)
auth.register_blueprint(b.bLogin, url_prefix='/auth')