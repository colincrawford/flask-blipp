from flask_blipp import __version__, flask_blipp
import pytest
from unittest.mock import Mock
from flask import Flask


@pytest.fixture
def app():
    app = Flask("test_app")

    @app.route("/", methods=["GET", "POST"])
    def home():
        pass

    @app.route("/a", methods=["GET", "PUT"])
    def a():
        pass

    return app


@pytest.fixture
def stdout_mock():
    return Mock()


def get_mock_stdout_output(stdout_mock):
    write_calls = [args[0][0] for args in stdout_mock.write.call_args_list]
    return "".join(write_calls)


def test_version():
    assert __version__ == "0.1.0"


def test_printing_to_stdout(app, stdout_mock):
    flask_blipp(app, output=stdout_mock)

    stdout_mock.write.assert_called()


def test_printing_routes(app, stdout_mock):
    flask_blipp(app, output=stdout_mock)
    routes_output = get_mock_stdout_output(stdout_mock)

    routes = [rule.rule for rule in app.url_map.iter_rules()]
    for route in routes:
        assert route in routes_output
