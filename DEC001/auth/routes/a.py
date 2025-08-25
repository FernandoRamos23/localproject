from flask import Blueprint
from flask import render_template, redirect
from flask import session, request

aLogin = Blueprint('aLogin', __name__)

@aLogin.route('/')
def indexLogin():
    mensaje = None
    if 'mensaje' in session:
        mensaje = session['mensaje']
    session.clear()
    return render_template('login.html', mensaje=mensaje)

@aLogin.route('/contacto')
def contacto():
    return render_template('contacto.html')

