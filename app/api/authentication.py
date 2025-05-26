from flask_restx import Namespace, Resource
from flask import request
from app.controllers.authentication import sign_up_player
import logging

from app.dto.auth import RegisterPlayerDTO
from app.utils.response_builder import ResponseBuilder


auth_ns = Namespace("auth", description="Authentication related operations.")
logger = logging.getLogger(__name__)


@auth_ns.route("/sign-up")
class PlayerSignUp(Resource):
    def post(self):  # type: ignore
        """
        Adds player to PostgreSQL database.
        """
        try:
            player_data = request.get_json()  # Request of user data
            logger.info(f"Trying to register new player: {player_data}")

            logger.info(f"Processing player data into dto")
            player_dto = RegisterPlayerDTO(**player_data)

            response = sign_up_player(player_dto)

            return response
        except Exception as e:
            return ResponseBuilder.error(
            message=f"Unexpected error happened when trying to register, player data: {player_data}",
            data={"error": str(e)}
        )    
