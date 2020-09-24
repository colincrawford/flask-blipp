import sys

from .basic_formatter import basic_formatter


def flask_blipp(app, output=sys.stdout, formatter=basic_formatter, ignored_http_methods=None):
    """
    Prints out the routes for a flask app on start up

    app - a flask app
    stdout - where to print the routes to
    """
    if not ignored_http_methods:
        ignored_http_methods = ["OPTIONS", "HEAD"]
    ignored_methods = set(ignored_http_methods)

    rules = [
        (rule, http_methods(rule.methods, ignored_methods))
        for rule in app.url_map.iter_rules()
    ]

    output.write(formatter(rules))


def http_methods(methods, ignored_methods):
    return [method for method in methods if method not in ignored_methods]
