import json
from .utils import generate_client_token, get_default_client_info

class MovieBoxAuth:
    def __init__(self, token: str = None, user_id: str = None):
        self.token = token
        self.user_id = user_id
        self.is_logged_in = bool(token)
        self.client_info = get_default_client_info()
        self.user_info = None

    def login_guest(self):
        self.token = None
        self.user_id = None
        self.is_logged_in = False
        self.user_info = None

    def update_session(self, token: str, user_id: str = None, user_info: dict = None):
        self.token = token
        self.user_id = user_id or self.user_id
        self.user_info = user_info or self.user_info
        self.is_logged_in = True

    def save_session(self):
        pass

    def load_session(self):
        pass

    def get_auth_headers(self) -> dict:
        headers = {
            "X-Client-Token": generate_client_token(),
            "X-Client-Status": "0",
            "X-Client-Info": json.dumps(self.client_info, separators=(",", ":")),
        }
        if self.is_logged_in and self.token:
            headers["Authorization"] = f"Bearer {self.token}"
            headers["X-Client-Status"] = "1"
            headers.pop("X-Client-Token", None)
        return headers
