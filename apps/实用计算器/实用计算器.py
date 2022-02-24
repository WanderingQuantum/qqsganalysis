from 破甲计算 import 计算防御值
from 元神属性计算 import 计算元神属性
from forms import 元神属性计算器表单, 破甲减破计算器表单
from extensions import db
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:qqsganalysis@localhost/qqsg'
db.init_app(app)


@app.route("/元神属性计算器", methods=['GET', 'POST'])
def 元神属性计算器():
    form = 元神属性计算器表单()
    if form.validate_on_submit():
        result = 计算元神属性(request.form)
        return render_template('元神属性计算器.html', form=form, result=result)
    return render_template('元神属性计算器.html', form=form, result={})


@app.route("/破甲减破计算器", methods=['GET', 'POST'])
def 破甲减破计算器():
    form = 破甲减破计算器表单()
    if form.validate_on_submit():
        result = 计算防御值(request.form)
        return render_template('破甲减破计算器.html', form=form, result=result)
    return render_template('破甲减破计算器.html', form=form, result={})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7890, debug=True)
