from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from dotenv import load_dotenv
import os

from app import create_app
from app.database.models import db


load_dotenv()

app = create_app(os.getenv("APP_SETTINGS", "config.Config"))

manager = Manager(app)
manager.add_command("db", MigrateCommand)
migrate = Migrate(app, db)


if __name__ == "__main__":
    manager.run()
