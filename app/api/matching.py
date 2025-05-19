from flask_restx import Namespace, Resource, fields
from flask import request
from app.controllers.matching import add_player_to_waitroom

matching_ns = Namespace('matching', description='Matching related operations')

@matching_ns.route('/waiting')
class Waiting(Resource):
    def post():
        """
        Adding user to waiting room.
        """
        data = request.get_json() 

        player_id = data['player_id']

        response = add_player_to_waitroom(player_id)
        
        return response     
