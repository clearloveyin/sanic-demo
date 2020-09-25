from __init__ import manager
from create_app import create_app

app = create_app()

manager.add_command('db', app.db.manager)
manager.add_command('runserver', app.run(host="0.0.0.0", port=9000))


if __name__ == "__main__":
    manager.run()