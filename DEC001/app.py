from flask import Flask


def DEC001():
    app = Flask(__name__)
    app.secret_key = "C@mil@19"

    from auth import auth
    from user import user
    from admin import admin

    app.register_blueprint(auth)
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(admin, url_prefix='/admin')

    return app


app = DEC001()
if __name__ == '__main__':
    app.run(debug=True)