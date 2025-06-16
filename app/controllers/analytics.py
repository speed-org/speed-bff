from flask import Response, current_app
import logging
from app.dto.analytics import AnalyticsEventDTO
from datetime import datetime

from app.dto.response_dto import ResponseDTO
from app.utils.response_builder import ResponseBuilder

logger = logging.getLogger(__name__)


def log_analytics_event(event_data: AnalyticsEventDTO) -> Response:
    """
    Logs event data into MongoDB database.
    """
    logger.info(f"Trying to log event data in mongodb, data:{event_data}")
    event_doc = {
        "event_type": event_data.event_type,
        "user_id": event_data.user_id,
        "data": event_data.data,
        "timestamp": datetime.utcnow(),
    }

    result = current_app.analytics_collection.insert_one(event_doc)

    # Convert ObjectId to string to avoid serialization error
    response_doc = event_doc.copy()
    response_doc["_id"] = str(result.inserted_id)

    return ResponseBuilder.success(
        message="Event data added to database", data=ResponseDTO(data=response_doc)
    )
