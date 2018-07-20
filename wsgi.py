# -*- coding: utf-8 -*-
"""
    novel.wsgi
    ----------

    for `flask run / flask shell / flask db migrate` file
    :copyright: (c) 2018-07-20 by buglan
"""

from flask_migrate import Migrate

from extensions import db
from novel import creat_app, models
# where import db and import models make `flask db migrate` work

app = creat_app('dev')
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(debug=True)
