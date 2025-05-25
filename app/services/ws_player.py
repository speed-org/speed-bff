from app import socketio
from app.models.event import EventBase
from dataclasses import asdict


class WsPlayerService:
    @staticmethod
    def emit_event_to_single_player(event: EventBase, sid: str) -> None:
        is_dict = isinstance(event.payload, dict)
        payload = event.payload if is_dict else asdict(event.payload)
        socketio.emit(event._type, payload, room=sid)
