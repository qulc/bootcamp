# Bootcamp

[![codecov](https://codecov.io/gh/qulc/bootcamp/branch/master/graph/badge.svg)](https://codecov.io/gh/qulc/bootcamp)


[![python](https://img.shields.io/badge/python-3.7-green.svg)](https://python.org)
[![django](https://img.shields.io/badge/django-2.1-green.svg)](https://www.djangoproject.com/)
[![graphql](https://img.shields.io/badge/graphene--django-2.1-green.svg)](https://github.com/graphql-python/graphene-django)

Bootcamp 学习 Django 和其它一些技术过程中的实践网站

### 预览: 

https://bootcamp.qulc.me/

### 在 Fork 上进行的修改
* GraphQL 的支持
* i18n 的国际化支持
* 支持游客身份访问
* 使用 cloudinary 服务处理图像
* 添加了单元测试和 CI 自动化部署
* 升级兼容最新的版本的 Django 和 Python

### 运行(需要安装 docker)
```bash
$ git clone https://github.com/qulc/bootcamp.git
$ cd bootcamp/

$ docker-compose up
# 浏览器打开 http://127.0.0.1:8000

# 运行测试
$ docker-compose exec web manage.py test
```
