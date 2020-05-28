from flask import Blueprint, render_template

bp_gedag = Blueprint('bp_gedag', __name__, url_prefix='',
                    template_folder='templates')

@bp_gedag.route('/')
def gedag():
   return render_template('gedag.html')

@bp_gedag.route("/later")
def later():
   return "later!"

@bp_gedag.route("/doei")
def doei():
    return render_template('doei.html')

