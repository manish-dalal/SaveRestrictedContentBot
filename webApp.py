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


if __name__ == "__main__":
    # run()
    #     p = Process(target=startWeb)
    #     p.start()
    #     # bot.run_until_disconnected()
    APP.run(host='0.0.0.0', port=PORT, debug=False)
