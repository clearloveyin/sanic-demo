from create_app import create_app
from blue.router_v1 import bp_v1

app = create_app()
app.blueprint(bp_v1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
