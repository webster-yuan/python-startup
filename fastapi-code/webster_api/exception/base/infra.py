class InfraException(Exception):
    status_code = 503
    detail = "Service unavailable"

    def __init__(self, detail: str | None = None):
        if detail:
            self.detail = detail
