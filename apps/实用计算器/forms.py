from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, BooleanField, RadioField, SelectField
from wtforms.validators import InputRequired, NumberRange


class 元神属性计算器表单(FlaskForm):
    当前物理攻击黄字点数 = DecimalField('当前物理攻击黄字点数', validators=[InputRequired(), NumberRange(min=0)], default=45)
    当前物理攻击成长 = DecimalField('当前物理攻击成长', validators=[InputRequired(), NumberRange(min=0, max=5.5)], default=3)
    当前法术攻击黄字点数 = DecimalField('当前法术攻击黄字点数', validators=[InputRequired(), NumberRange(min=0)], default=45)
    当前法术攻击成长 = DecimalField('当前法术攻击成长', validators=[InputRequired(), NumberRange(min=0, max=5.5)], default=3)
    当前物理防御黄字点数 = DecimalField('当前物理防御黄字点数', validators=[InputRequired(), NumberRange(min=0)], default=45)
    当前物理防御成长 = DecimalField('当前物理防御成长', validators=[InputRequired(), NumberRange(min=0, max=5.5)], default=3)
    当前法术防御黄字点数 = DecimalField('当前法术防御黄字点数', validators=[InputRequired(), NumberRange(min=0)], default=45)
    当前法术防御成长 = DecimalField('当前法术防御成长', validators=[InputRequired(), NumberRange(min=0, max=5.5)], default=3)
    当前攻击配合黄字点数 = DecimalField('当前攻击配合黄字点数', validators=[InputRequired(), NumberRange(min=0)], default=480)
    当前攻击配合成长 = DecimalField('当前攻击配合成长', validators=[InputRequired(), NumberRange(min=0, max=5.5)], default=3)
    当前防御配合黄字点数 = DecimalField('当前防御配合黄字点数', validators=[InputRequired(), NumberRange(min=0)], default=400)
    当前防御配合成长 = DecimalField('当前防御配合成长', validators=[InputRequired(), NumberRange(min=0, max=5.5)], default=3)
    当前等级 = IntegerField('当前等级', validators=[InputRequired(), NumberRange(min=1)], default=1)

    等级 = IntegerField('等级', validators=[InputRequired(), NumberRange(min=1)], default=1)
    物理攻击手动分配点数 = DecimalField('物理攻击手动分配点数', validators=[InputRequired(), NumberRange(min=0)], default=0)
    法术攻击手动分配点数 = DecimalField('法术攻击手动分配点数', validators=[InputRequired(), NumberRange(min=0)], default=0)
    物理防御手动分配点数 = DecimalField('物理防御手动分配点数', validators=[InputRequired(), NumberRange(min=0)], default=0)
    法术防御手动分配点数 = DecimalField('法术防御手动分配点数', validators=[InputRequired(), NumberRange(min=0)], default=0)
    攻击配合手动分配点数 = DecimalField('攻击配合手动分配点数', validators=[InputRequired(), NumberRange(min=0)], default=0)
    防御配合手动分配点数 = DecimalField('防御配合手动分配点数', validators=[InputRequired(), NumberRange(min=0)], default=0)
    物理攻击融合点数 = DecimalField('物理攻击融合点数', validators=[InputRequired(), NumberRange(min=0)], default=0)
    法术攻击融合点数 = DecimalField('法术攻击融合点数', validators=[InputRequired(), NumberRange(min=0)], default=0)
    物理防御融合点数 = DecimalField('物理防御融合点数', validators=[InputRequired(), NumberRange(min=0)], default=0)
    法术防御融合点数 = DecimalField('法术防御融合点数', validators=[InputRequired(), NumberRange(min=0)], default=0)
    物理攻击成长 = DecimalField('物理攻击成长', validators=[InputRequired(), NumberRange(min=0, max=5.5)], default=3)
    法术攻击成长 = DecimalField('法术攻击成长', validators=[InputRequired(), NumberRange(min=0, max=5.5)], default=3)
    物理防御成长 = DecimalField('物理防御成长', validators=[InputRequired(), NumberRange(min=0, max=5.5)], default=3)
    法术防御成长 = DecimalField('法术防御成长', validators=[InputRequired(), NumberRange(min=0, max=5.5)], default=3)


class 破甲减破计算器表单(FlaskForm):
    总物防 = IntegerField('总物防', validators=[InputRequired(), NumberRange(min=0)], default=0)
    总法防 = IntegerField('总法防', validators=[InputRequired(), NumberRange(min=0)], default=0)
    元神物防 = IntegerField('元神物防', validators=[InputRequired(), NumberRange(min=0)], default=0)
    元神法防 = IntegerField('元神法防', validators=[InputRequired(), NumberRange(min=0)], default=0)
    八阵图物防 = IntegerField('八阵图物防', validators=[InputRequired(), NumberRange(min=0)], default=0)
    八阵图法防 = IntegerField('八阵图法防', validators=[InputRequired(), NumberRange(min=0)], default=0)

    元神破甲 = BooleanField('元神破甲')
    雪莲怒凋 = BooleanField('雪莲怒凋')
    当阳怒吼 = BooleanField('当阳怒吼')
    断魂 = BooleanField('断魂')
    断魂等级 = SelectField('断魂等级',
                       choices=[(1, '1阶蓝断魂'), (2, '2阶蓝断魂'), (2, '1阶紫断魂'), (3, '2阶紫断魂'), (4, '3阶紫断魂')],
                       default=4)
    虎虎生威 = BooleanField('虎虎生威')
    铜台锁梦 = BooleanField('铜台锁梦')
    铜台锁梦阶层 = SelectField('铜台锁梦阶层', choices=[(9, '9阶铜台锁梦'), (10, '10阶铜台锁梦')], default=10)
    八阵图青龙破甲 = BooleanField('八阵图青龙破甲')
    八阵图青龙破甲阶层 = SelectField('八阵图青龙破甲阶层',
                            choices=[(1, '1阶'), (2, '2阶'), (3, '3阶'), (4, '4阶'), (5, '5阶'), (6, '6阶')],
                            default=4)
    天狼爪 = BooleanField('天狼爪')
    天狼爪等级 = SelectField('天狼爪等级',
                        choices=[(1, '1级'), (2, '2级'), (3, '3级'), (4, '4级'), (5, '5级')],
                        default=5)
    天狼爪连球数 = SelectField('天狼爪连球数',
                         choices=[(1, '1连球'), (2, '2连球'), (3, '3连球')],
                         default=1)

    奥义护体之神 = BooleanField('奥义护体之神')
    奥义护体之神减破百分比 = IntegerField('奥义护体之神减破百分比', validators=[NumberRange(min=0, max=100)], default=20)
    子女藤甲 = BooleanField('子女藤甲')
    子女藤甲减破百分比 = DecimalField('子女藤甲减破百分比', validators=[NumberRange(min=0, max=100)], default=15)
    坚韧之灵 = BooleanField('坚韧之灵')
    坚韧之灵减破百分比 = IntegerField('坚韧之灵减破百分比', validators=[NumberRange(min=0, max=100)], default=40)
    韧性 = IntegerField('韧性', validators=[InputRequired(), NumberRange(min=0, max=50)], default=50)
    夫妻等级 = IntegerField('夫妻等级', validators=[InputRequired(), NumberRange(min=15, max=20)], default=20)
