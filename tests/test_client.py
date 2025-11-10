import pytest
from exvo.client import ExvoClient

def test_client_base_url():
    c = ExvoClient(base_url="http://example.com")
    assert c.base == "http://example.com"

# The next tests require a running exvo-core; these are basic smoke checks when integrated.
