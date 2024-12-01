from flask import Flask
from dotenv import load_dotenv

from betsapp import routes, database, config

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()
    app.config.from_object("betsapp.config.DevelopmentConfig")

    database.init_app(app)
    # print(database.test(app))

    app.register_blueprint(routes.bp)

    #config.AzureKV(app)
    
    return app

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000, debug=True)
