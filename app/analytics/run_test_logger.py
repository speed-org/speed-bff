from app import create_app
from app.config import Config
from app.analytics import logger as analytics_logger

app = create_app(Config())


def test() -> None:
    with app.app_context():
        analytics_logger.log_event(
            event_type="test_event",
            user_id="debug123",
            data={"test_field": "hello", "value": 42},
        )
        print("Test event logged to MongoDB!")
