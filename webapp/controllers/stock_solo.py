from flask import Blueprint,redirect,render_template,url_for
from os import path
from webapp.models import stock_basics
from webapp.forms import CodeForm
from flask_login import login_required,current_user
from webapp.extensions import finance_analyst_permission
stocksolo_blueprint = Blueprint(
    'stock_solo',
    __name__,
    template_folder=path.join(path.pardir,'templates','stock_solo'),
    url_prefix="/stock_solo"
)
@stocksolo_blueprint.route('/',methods=('GET','POST'))
@stocksolo_blueprint.route('/<string:trade_code>',methods=('GET','POST'))
@login_required
@finance_analyst_permission.require(http_exception=403)
def home(trade_code='000001'):
    trade_code=trade_code
    form = CodeForm()
    if form.validate_on_submit():
        trade_code = form.code.data
        return redirect(url_for('stock_solo.home',current_user=current_user,trade_code=trade_code))
    stock = stock_basics.query.filter_by(trade_code=trade_code).first_or_404()
    return render_template("stock_solo/stock_solo_home.html",current_user=current_user,form=form,stock = stock)