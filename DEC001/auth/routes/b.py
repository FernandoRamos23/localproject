from flask import Blueprint
from flask import render_template, request, redirect, session

bLogin = Blueprint('bLogin', __name__)

# '/auth/' prefijo de ruta

@bLogin.route('/', methods=['GET', 'POST']) 
def indexB():
    session.clear()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        session['login'] = username, password
        return redirect('/auth/login')
    session['mensaje'] = 'Error inesperado'
    return redirect('/')


@bLogin.route('/login')
def login():
    print(session)
    username, password = session['login'] if 'login' in session else (None, None)
    session.clear()
    if username == 'admin' and password == 'admin':
        session['session'] = (True, 'admin')
        return redirect('/admin')
    elif username == 'user' and password == 'user':
        session['session'] = (True, 'user')
        return redirect('/user')
    session['mensaje'] = 'Credenciales invalidas'
    return redirect('/')

@bLogin.route('/contacto')
def contacto():
    return render_template('contacto.html')
