from sanic import Sanic
from sanic_script import Manager
from sanic_pw import Peewee

app = Sanic(name='user-server')
app.db = Peewee(app)
manager = Manager(app)
