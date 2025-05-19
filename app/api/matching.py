from flask_restx import Namespace, Resource
from flask import request
from app.controllers.matching import add_player_to_waitroom
import logging

matching_ns = Namespace('matching', description='Matching related operations')
logger = logging.getLogger(__name__)

@matching_ns.route('/waiting')
class Waiting(Resource):
    def post(self):
        """
        Adding user to waiting room.
        """
        logger.debug('Got to the endpoint')
        data = request.get_json() 

        player_id = data['player_id']
        logger.debug(f'Player id: {player_id}')

        response = add_player_to_waitroom(player_id)
        
        return response     
