from flask import Flask
from os import path

def create_app():
    app = Flask(__name__) #name of the file initializes flask
    app.config['SECRET_KEY'] = 'ijsdoijafopoafkf' #secures website with random string

    from .views import views
    from .results import results3
    from .results import results2,results12, results13, results14, results31
    from .results import results1, results4, results5, results6, results7, results8, results9, results10, results11
    from .results import results15, results16, results17, results18, results19, results20, results21, results22, results23
    from .results import results42, results32, results24, results25, results26, results27, results28, results29, results30
    from .results import results33, results34, results35, results36, results37, results38, results39, results40
    from .results import results41, results43, results44, results45, results46


    app.register_blueprint(views, url_prefix='/') #access with / "name of page"
    app.register_blueprint(results3, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results2, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results1, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results4, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results5, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results6, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results7, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results8, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results9, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results10, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results11, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results12, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results13, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results14, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results15, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results16, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results17, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results18, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results19, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results20, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results21, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results22, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results23, url_prefix='/')  # access with / "name of page"

    app.register_blueprint(results24, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results25, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results26, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results27, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results28, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results29, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results30, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results31, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results32, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results33, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results34, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results35, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results36, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results37, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results38, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results39, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results40, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results41, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results42, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results43, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results44, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results45, url_prefix='/')  # access with / "name of page"
    app.register_blueprint(results46, url_prefix='/')  # access with / "name of page"


    return app

