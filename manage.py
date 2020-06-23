import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import create_app, db
from app.models import *


app = create_app()
app.app_context().push()
manager = Manager(app)
migrate = Migrate(app, db)


# database cli command
manager.add_command('db', MigrateCommand)


# start Flask app command
@manager.command
def run():
	app.run()


if __name__ == "__main__":
	manager.run()
