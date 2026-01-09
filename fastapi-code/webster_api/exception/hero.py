from webster_api.exception.base import BusinessException


class HeroNotFoundError(BusinessException):
    status_code = 404
    detail = "Hero not found"
