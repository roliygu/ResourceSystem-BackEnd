# ResourceSystem-BackEnd
资源管理系统的后端项目


### 1 安装

安装python相关依赖包
```
# 项目根目录下
bash scripts/setup.sh
```

初始化数据库
```
python3 manage.py shell
>>> from app import create_app, db
>>> db.create_all()
>>> db.drop_all()
```