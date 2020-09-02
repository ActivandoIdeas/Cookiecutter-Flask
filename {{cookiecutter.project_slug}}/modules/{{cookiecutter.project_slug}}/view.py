from flask import Blueprint
from modules.root.models import Msg

{{cookiecutter.project_slug}}_view = Blueprint('{{cookiecutter.project_slug}}',
                      __name__,
                      url_prefix='/',
                      template_folder='templates',
                      static_folder='static')


@{{cookiecutter.project_slug}}_view.route("/")
def {{cookiecutter.project_slug}}_app():
    a = Msg.query.all()
    expose = '';
    for i in a:
        expose += i.name

    return f"Hello World: {expose}"
