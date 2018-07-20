# -*- coding: utf-8 -*-
"""
    novel.__init__
    --------------

    flask application initialize
    :copyright: (c) 2018-07-20 by buglan
"""

from flask import Flask

from config import config
from extensions import db


def creat_app(config_name):
    """creat_app

    :param config_name:config name such as 'dev'
    """
    app = Flask(__name__)

    # the location is important
    app.config.from_object(config[config_name])
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
