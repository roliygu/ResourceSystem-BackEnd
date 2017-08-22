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
1. 下载功能
    集成下载按钮，下载url使用origin_name,这样下载另存为的文件名默认是origin_name
2. 调整样式
3. 上传之后，时间戳显示问题
5. table python model重构
6. 检索功能
7. 分页功能
8. 删除资源
9. 修改资源

标签管理
1. 新增标签管理页面

上传资源
1. 选择已有的标签。因为标签是一个比较重的功能，所以不在此页面直接创建标签。

数据库
1. 重构数据库及其model
2. 思考数据库升级，数据迁移方案