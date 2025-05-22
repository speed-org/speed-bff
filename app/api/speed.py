from flask_restx import Namespace, Resource

speed_ns = Namespace("speed", description="Speed API operations")


@speed_ns.route("/")
class NewGame(Resource):
    def post(self) -> tuple:
        """
        Create a new game.
        """
        # Here you would typically create a new game in your database
        # For this example, we'll just return a success message
        return {"message": "New game created!"}, 201
