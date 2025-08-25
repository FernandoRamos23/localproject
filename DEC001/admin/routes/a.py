from flask import Blueprint
from flask import render_template, redirect
from flask import session, request

aAdmin = Blueprint('aAdmin', __name__)

@aAdmin.route('/')
def indexAdmin():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if isValid and user == 'admin':
        return redirect('/admin/dashboard')
    return 'acceso no autorizado', 403

@aAdmin.route('/dashboard')
def dashboardAdmin():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if not isValid and user != 'admin':
        return redirect('/')
    return render_template('dashboardAdmin.html')

@aAdmin.route('/caja')
def cajaAdmin():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if not isValid and user != 'admin':
        return redirect('/')
    return "caja admin"

@aAdmin.route('/productos')
def productosAdmin():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if not isValid and user != 'admin':
        return redirect('/')
    return "productos admin"

@aAdmin.route('/reportes')
def reportesAdmin():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if not isValid and user != 'admin':
        return redirect('/')
    return "reportes admin"

@aAdmin.route('/movimientos')
def movimientosAdmin():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if not isValid and user != 'admin':
        return redirect('/')
    return "movimientos admin"

@aAdmin.route('cierre-caja')
def cierre_cajaAdmin():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if not isValid and user != 'admin':
        return redirect('/')
    return "cierre-caja admin"

@aAdmin.route('/logout')
def logoutAdmin():
    session.clear()
    return redirect('/')