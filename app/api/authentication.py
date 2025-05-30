from typing import Optional
from flask_restx import Namespace, Resource
from flask import request
from app.controllers.authentication import sign_up_player, log_in_player
import logging

from app.dto.auth import RegisterPlayerPayloadDTO, LogInPlayerPayloadDTO
from app.dto.response_dto import ResponseDTO
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

            logger.info("Processing player data into dto")
            player_dto = RegisterPlayerPayloadDTO(**player_data)

            response = sign_up_player(player_dto)

            return response
        except Exception as e:
            return ResponseBuilder.error(
                message=(
                    f"Unexpected error happened when trying to register,"
                    f" player data: {player_data}"
                ),
                data=ResponseDTO(error = str(e)),
            )


@auth_ns.route("/log-in")
class PlayerLogIn(Resource):
    def get(self):  # type: ignore
        """
        Retreives player's information from PostgreSQL database.
        """
        try:
            firebase_id = request.args.get('firebaseId')
            logger.info(f"Trying to retrieve data of player: {firebase_id}")

            if not firebase_id:
                message = "Missing firebase_id"
                logger.error(message)
                ResponseBuilder.fail(message)

            logger.info("Processing player data into dto")
            player_dto = LogInPlayerPayloadDTO(str(firebase_id))

            response = log_in_player(player_dto)

            return response
        except Exception as e:
            return ResponseBuilder.error(
                message=(
                    f"Unexpected error happened when trying to retrieve data by firebase_id,"
                    f" player data: {firebase_id}"
                ),
                data=ResponseDTO(error = str(e)),
            )
