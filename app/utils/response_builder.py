from typing import Optional
from flask import jsonify, make_response, Response
from app.utils.constants import RequestKey, HttpStatus
from app.dto.response_dto import ResponseDTO
from dataclasses import asdict


class ResponseBuilder:
    @staticmethod
    def success(
        message: str = "Operation successful",
        data: Optional[ResponseDTO] = None,
        status_code: int = HttpStatus.SUCCESS.value,
    ) -> Response:
        response_data = {
            RequestKey.STATUS.value: "success",
            RequestKey.MESSAGE.value: message,
            RequestKey.DATA.value: asdict(data) if data else None,
        }

        return make_response(jsonify(response_data), status_code)

    @staticmethod
    def fail(
        message: str = "Operation failed",
        data: Optional[ResponseDTO] = None,
        status_code: int = HttpStatus.BAD_REQUEST.value,
    ) -> Response:
        response_data = {
            RequestKey.STATUS.value: "fail",
            RequestKey.MESSAGE.value: message,
            RequestKey.DATA.value: asdict(data) if data else None,
        }

        return make_response(jsonify(response_data), status_code)

    @staticmethod
    def error(
        message: str = "Internal server error",
        data: Optional[ResponseDTO] = None,
        status_code: int = HttpStatus.INTERNAL_SERVER_ERROR.value,
    ) -> Response:
        response_data = {
            RequestKey.STATUS.value: "error",
            RequestKey.MESSAGE.value: message,
            RequestKey.DATA.value: asdict(data) if data else None,
        }

        return make_response(jsonify(response_data), status_code)
