from flask import Blueprint, render_template

bp_spelers = Blueprint('bp_spelers', __name__, url_prefix='/spelers',
                    template_folder='templates')

@bp_spelers.route('/')
def spelers():
   return render_template('spelers.html')