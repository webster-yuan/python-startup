class BusinessException(Exception):
    status_code = 400
    detail = "Business error"

    def __init__(self, detail: str | None = None):
        if detail:
            self.detail = detail
