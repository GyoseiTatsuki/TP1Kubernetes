from flask import Flask # type: ignore

from project.api import api


def create_app():
    app = Flask(__name__)
    api.init_app(app)
    return app

POSTGRES_URL = "postgresql://appcrud:1234321@postgres-db.database.svc.cluster.local:5432/messages"
