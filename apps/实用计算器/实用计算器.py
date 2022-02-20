from 破甲计算 import 计算防御值
from forms import 破甲减破计算器表单
from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
csrf = CSRFProtect(app)


@app.route("/破甲减破计算器", methods=['GET', 'POST'])
def 破甲减破计算器():
    form = 破甲减破计算器表单()
    if form.validate_on_submit():
        result = 计算防御值(request.form)
        return render_template('破甲减破计算器.html', form=form, result=result)
    return render_template('破甲减破计算器.html', form=form, result={})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7890, debug=True)
