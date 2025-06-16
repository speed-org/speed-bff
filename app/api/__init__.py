from flask_restx import Api
from app.api.speed import speed_ns
from app.api.matching import matching_ns
from app.api.authentication import auth_ns
from app.api.analytics import analytics_ns

api = Api(
    title="Flask REST API",
    version="1.0",
    description="A simple Flask REST API",
)

api.add_namespace(speed_ns, path="/speed")
api.add_namespace(matching_ns, path="/matching")
api.add_namespace(auth_ns, path="/auth")
api.add_namespace(analytics_ns, path="/analytics")
