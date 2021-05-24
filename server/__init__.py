import os
from flask import Flask

#各種設定
from .config import APP_NAME, JSON_AS_ASCII

app = Flask(__name__)

def setup_app():
    app.config['RESTX_MASK_SWAGGER'] = False
    app.config['ERROR_INCLUDE_MESSAGE'] = False

    from .page.main import main

    #static(images/css/js)
    from .page.static import static

    #API
    from .api import api

    app.config["JSON_AS_ASCII"] = JSON_AS_ASCII
    app.register_blueprint(static, url_prefix='/static')

    from .tool.filter import main

    return app
