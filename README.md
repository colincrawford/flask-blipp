# flask-blipp
[![CircleCI](https://circleci.com/gh/colinlcrawford/flask-blipp.svg?style=svg)](https://circleci.com/gh/colinlcrawford/flask-blipp)
[![Coverage Status](https://coveralls.io/repos/github/colinlcrawford/flask-blipp/badge.svg?branch=master)](https://coveralls.io/github/colinlcrawford/flask-blipp?branch=master)

Logs out the HTTP routes for a flask app

usage:
```python
from flask import Flask
from flask_blipp import flask_blipp

app = Flask(__name__)
flask_blipp(app)
```

Helpful links:

https://github.com/pallets/werkzeug/blob/master/src/werkzeug/routing.py#L514
https://werkzeug.palletsprojects.com/en/0.16.x/routing/#werkzeug.routing.Map
