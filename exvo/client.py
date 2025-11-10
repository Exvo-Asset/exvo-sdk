import requests
from typing import Optional

class ExvoClient:
    def __init__(self, base_url: str = "http://localhost:8000", token: Optional[str] = None, timeout: int = 10):
        self.base = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout

    def _headers(self):
        h = {"Accept": "application/json"}
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        return h

    def list_assets(self):
        url = f"{self.base}/v1/assets/"
        r = requests.get(url, headers=self._headers(), timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def get_snapshot(self, symbol: str):
        url = f"{self.base}/v1/markets/snapshot/{symbol}"
        r = requests.get(url, headers=self._headers(), timeout=self.timeout)
        r.raise_for_status()
        return r.json()
