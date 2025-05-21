from flask_restx import Api
from app.api.speed import speed_ns

api = Api(
    title="Flask REST API",
    version="1.0",
    description="A simple Flask REST API",
)

api.add_namespace(speed_ns, path="/speed")
