import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def app(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"<h1>Hello, World!</h1>"]