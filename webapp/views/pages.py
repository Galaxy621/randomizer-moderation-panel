from flask import Blueprint, render_template

bp = Blueprint('pages', __name__)

@bp.route('/')
def index():
    return render_template('pages/index.html.j2')