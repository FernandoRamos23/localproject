from flask import Blueprint
from flask import render_template, redirect
from flask import request, session


aUser = Blueprint('aUser', __name__)

'''
/user/  <- prefijo usuario
'''
@aUser.route('/')
def indexUser():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if isValid and user == 'user':
        return redirect('/user/dashboard')
    return 'acceso no autorizado', 403

@aUser.route('/dashboard')
def dashboard():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if not isValid and user != 'user':
        return redirect('/logout')
    return render_template('dashboardUser.html')

@aUser.route('/caja')
def caja():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if not isValid and user != 'user':
        return redirect('/logout')
    return render_template('caja.html')

@aUser.route('/productos')
def productos():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if not isValid and user != 'user':
        return redirect('/logout')
    return "productos user"

@aUser.route('/reportes')
def reportes():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if not isValid and user != 'user':
        return redirect('/logout')
    return "reportes user"

@aUser.route('/movimientos')
def movimientos():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if not isValid and user != 'user':
        return redirect('/logout')
    return "movimientos user"

@aUser.route('cierre-caja')
def cierre_caja():
    isValid, user = session['session'] if 'session' in session else (False, None)
    if not isValid and user != 'user':
        return redirect('/logout')
    return "cierre-caja user"

@aUser.route('/logout')
def logout():
    session.clear()
    return redirect('/')