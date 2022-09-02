import os
import re
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:qqsganalysis@localhost/qqsg')


def 导入解包数据():
    for root, dirs, files in os.walk('解包数据/整理后数据'):
        for name in files:
            match = re.search(r'\(([^\.]*)\.txt\).xlsx', name)
            if match:
                print(os.path.join(root, name))
                print(match.group(1))
                data = pd.read_excel(os.path.join(root, name))
                data.to_sql(match.group(1), engine, if_exists='replace')


def 导入测试数据():
    from 元神属性点数与属性百分比对应表 import 元神属性点数与属性百分比对应表
    data = pd.DataFrame({'属性点数': list(range(3501)), '属性百分比': 元神属性点数与属性百分比对应表})
    data.to_sql('元神属性点数与属性百分比对应表', engine, if_exists='replace')


if __name__ == '__main__':
    导入解包数据()
    导入测试数据()
