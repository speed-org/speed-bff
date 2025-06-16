from flask_restx import Namespace, Resource
from flask import request
from app.controllers.matching import add_player_to_matching_system, match_oldest_players
import logging
from app.analytics.run_test_logger import test


matching_ns = Namespace("matching", description="Matching related operations")
logger = logging.getLogger(__name__)


@matching_ns.route("/waiting")
class Waiting(Resource):
    def post(self):  # type: ignore
        """
        Adding player to waiting room.
        """
        logger.debug("Got to the waiting endpoint")
        data = request.get_json()  # Request of player ID

        # Testing analytics logger rq
        test()

        player_id = data["player_id"]
        logger.debug(f"Player id: {player_id}")
        response = add_player_to_matching_system(player_id)

        return response


@matching_ns.route("/matching")
class Matching(Resource):
    def get(self):  # type: ignore
        """
        Matching two oldest players.
        """
        logger.debug("Got to the matching endpoint")
        response = match_oldest_players()

        return response
