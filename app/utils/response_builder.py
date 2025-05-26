from typing import Any, Optional
from flask import jsonify, make_response
from app.utils.constants import RequestKey, HttpStatus


class ResponseBuilder:
    @staticmethod
    def success(message: str = "Operation successful", data: Any = None, status_code: int = HttpStatus.SUCCESS.value):
        response_data = {
            RequestKey.STATUS.value: "success",
            RequestKey.MESSAGE.value: message,
            RequestKey.DATA.value: data
        }

        return make_response(jsonify(response_data), status_code)

    @staticmethod
    def fail(message: str = "Operation failed", data: Optional[Any] = None, status_code: int = HttpStatus.BAD_REQUEST.value):
        response_data = {
            RequestKey.STATUS.value: "fail",
            RequestKey.MESSAGE.value: message,
            RequestKey.DATA.value: data
        }
        
        return make_response(jsonify(response_data), status_code)

    @staticmethod
    def error(
        message: str = "Internal server error",
        code: Optional[str] = None,
        data: Optional[Any] = None,
        status_code: int = HttpStatus.INTERNAL_SERVER_ERROR.value,
    ):
        response_data = {
            RequestKey.STATUS.value: "error",
            RequestKey.MESSAGE.value: message,
            RequestKey.DATA.value: data
        }

        if code:
            response_data[RequestKey.CODE.value] = code

        return make_response(jsonify(response_data), status_code)