import click
import config
from app import create_app

from flask import Flask
from flask.cli import FlaskGroup, with_appcontext

cli = FlaskGroup(create_app=create_app)

@cli.command('_')
@with_appcontext
def custom_command():
    pass
    # from scripts._ import _Command
    # cmd = _Command()
    # cmd.run()

if __name__ == "__main__":
    cli()