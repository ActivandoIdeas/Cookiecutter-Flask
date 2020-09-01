from flask import Blueprint
from modules.root.models import Migration

root_view = Blueprint('root',
                      __name__,
                      url_prefix='/',
                      template_folder='templates',
                      static_folder='static')


@root_view.route("/")
def root_app():
    a = Migration.query.all()
    for i in a:
        print(i.name)

    return "Hello World"
