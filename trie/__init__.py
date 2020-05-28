from flask import Flask
from trie import cli
from trie.bp_gedag import bp_gedag
from trie.bp_spelers import bp_spelers
from trie.database import db

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    uri='sqlite:///%s/%s.db' % (app.instance_path , __name__ )
    app.config.from_mapping(
        SQLALCHEMY_TRACK_MODIFICATIONS='false',
        SQLALCHEMY_DATABASE_URI=uri,
        SECRET_KEY='DEV',
        APP_VERSION='set APP_VERSION in instance config')

    app.config.from_pyfile('config.cfg', silent=False)

    db.init_app(app)
    init_app(app)


    app.register_blueprint(bp_gedag)
    app.register_blueprint(bp_spelers)
    return app

def init_app(app):
    cli.init_cli_commands(app)
   
    
