from typing import Optional
from flask import request
from app.utils.constants import WS_EVENT_HANDLER_FIELD


def get_player_id_from_request() -> Optional[str]:
    return request.args.get(WS_EVENT_HANDLER_FIELD.USER_ID.value)


def get_player_sid_from_request() -> str:
    sid: str = request.sid  # type: ignore
    return sid
