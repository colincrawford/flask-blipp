import sys


def flask_blipp(app, stdout=sys.stdout, ignore_head=True, ignore_options=True):
    """
    Prints out the routes for a flask app on start up

    app - a flask app
    stdout - where to print the routes to
    """
    rules = [rule for rule in app.url_map.iter_rules()]
    for rule in rules:
        for method in rule.methods:
            if method == "OPTIONS" and ignore_options:
                continue
            if method == "HEAD" and ignore_head:
                continue
            stdout.write(f"{method} {rule}\n")
