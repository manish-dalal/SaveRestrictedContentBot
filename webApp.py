from gunicorn.app.wsgiapp import WSGIApplication
from flask import Flask
from decouple import config

PORT = config("PORT", default=None)

# Function that create the app


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    # Simple route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app  # do not forget to return the app


APP = create_app()


def startWeb():
    print('Hello start web')
    # APP.run(host='0.0.0.0', port=5000, debug=True)
    APP.run(debug=False)


class StandaloneApplication(WSGIApplication):
    def __init__(self, app_uri, options=None):
        self.options = options or {}
        self.app_uri = app_uri
        super().__init__()

    def load_config(self):
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)


def run():
    url = "0.0.0.0:" + PORT
    options = {
        "bind": url,
        "workers": 1
    }
    StandaloneApplication("webApp:create_app()", options).run()


if __name__ == "__main__":
    run()
#     p = Process(target=startWeb)
#     p.start()
#     # bot.run_until_disconnected()
#     # APP.run(host='0.0.0.0', port=5000, debug=True)
