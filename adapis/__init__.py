from flask import Flask, current_app


def create_app():
    app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/mydb.sqlite3'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from adapis.app import blueprint
    app.register_blueprint(blueprint, url_prefix='/api')

    # from adapis.app import api
    # api.init_app(app)

#     from adapis.app.dbapp import db
#     db.init_app(app)

    return app


# def app_db():
#     appdb = Flask(__name__)
#     appdb.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/mydb.sqlite3'
#     appdb.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     from adapis.app.dbapp import db
#     db.init_app(appdb)

#     return appdb
