from extensions import db


class 元神属性点数与属性百分比对应表(db.Model):
    属性点数 = db.Column(db.Integer, primary_key=True)
    属性百分比 = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<{self.属性点数}, {self.属性百分比}>'
