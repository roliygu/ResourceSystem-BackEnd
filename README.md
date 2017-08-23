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

### 2 开发功能与计划

预览页面
2. 调整样式
7. 分页功能
9. 修改资源(还差修改标签)

标签管理
1. 新增标签管理页面

数据库
2. 思考数据库升级，数据迁移方案

优化
按照restful的风格建立json交互机制，分拆渲染模板，提供缓存机制