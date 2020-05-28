import click
from flask import current_app, g
from flask.cli import with_appcontext
from trie.models import spelers_models
from trie.database import db

def init_db():
    db.create_all()


def fill_db():
    db.drop_all()
    db.create_all()

    db.session.add(spelers_models.Spelers('Rianne', 'Bos', 8))
    db.session.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database %s.' %
               current_app.config['SQLALCHEMY_DATABASE_URI'])

@click.command('fill-db')
@with_appcontext
def fill_db_command():
    """Clear the existing data and create new tables."""
    fill_db()
    click.echo('Cleaning and added test data to database %s.' %
               current_app.config['SQLALCHEMY_DATABASE_URI'])

def init_cli_commands(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(fill_db_command)               