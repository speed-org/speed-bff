from typing import Any, Optional
from flask import current_app
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def log_event(event_type: str, user_id: str, data: Optional[dict[str, Any]]) -> None:
    """
    Logs an analytics event to MongoDB.
    """
    event_doc = {
        "event": event_type,
        "user_id": user_id,
        "timestamp": datetime.utcnow(),
    }

    # Adds more keys to Mongo doc
    if data:
        event_doc.update(data)

    logger.info(
        f"Logging analytics event: {event_type} for user {user_id} with data: {data}"
    )

    try:
        # Saving to
        current_app.analytics_collection.insert_one(event_doc)
        logger.info("Analytics event successfully logged.")
    except Exception as e:
        logger.error(
            f"Unexpected error while logging event: {event_type} for user {user_id}. "
            f"Data: {data}. Error: {e}"
        )
        raise
