from flask import request
from flask_restx import Namespace, Resource
import logging
from app.controllers.analytics import log_analytics_event
from app.dto.response_dto import ResponseDTO
from app.utils.response_builder import ResponseBuilder
from app.dto.analytics import AnalyticsEventDTO

analytics_ns = Namespace("analytics", description="Analytics related operations.")
logger = logging.getLogger(__name__)


@analytics_ns.route("/log")
class AnalyticsLogger(Resource):
    def post(self):  # type: ignore
        """
        Logs a custom analytics event.
        """
        try:
            event_data = request.get_json()
            logger.info(f"Trying to log analytics data: {event_data}")

            logger.info("Processing event data into dto")
            event_dto = AnalyticsEventDTO(**event_data)

            response = log_analytics_event(event_dto)

            return response
        except Exception as e:
            return ResponseBuilder.error(
                message=(
                    f"Unexpected error happened when trying to log data,"
                    f" event data: {event_data}"
                ),
                data=ResponseDTO(error=str(e)),
            )
