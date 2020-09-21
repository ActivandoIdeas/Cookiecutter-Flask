from flask import Blueprint
from modules.example.models import Msg

example_view = Blueprint('example',
                         __name__,
                         url_prefix='/',
                         template_folder='templates',
                         static_folder='static')


@example_view.route("/")
def example_app():
    """Simple function to test example"""
    a = Msg.query.all()
    msg = ''
    for i in a:
        msg += i.name

    return f"Hello World: {msg}"
