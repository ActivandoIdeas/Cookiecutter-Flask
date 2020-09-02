from flask import Blueprint
from modules.root.models import Msg

root_view = Blueprint('root',
                      __name__,
                      url_prefix='/',
                      template_folder='templates',
                      static_folder='static')


@root_view.route("/")
def root_app():
    a = Msg.query.all()
    expose = '';
    for i in a:
        expose += i.name

    return f"Hello World: {expose}"
