from flask import Blueprint
from modules.{{cookiecutter.project_slug}}.models import Msg

{{cookiecutter.project_slug}}_view = Blueprint('{{cookiecutter.project_slug}}',
                      __name__,
                      url_prefix='/',
                      template_folder='templates',
                      static_folder='static')


@{{cookiecutter.project_slug}}_view.route("/")
def {{cookiecutter.project_slug}}_app():
    """Simple function to test app"""
    a = Msg.query.all()
    msg = ''
    for i in a:
        msg += i.name

    return f"Hello World: {msg}"
