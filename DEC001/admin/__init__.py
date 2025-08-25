from flask import Blueprint
from .routes import a

admin = Blueprint(
    'admin',
    __name__,  # ← esto es clave
    template_folder='templates',
    static_folder='static',
    static_url_path='/admin/static'
)

admin.register_blueprint(a.aAdmin)