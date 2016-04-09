## Bootcamp是一个[Python Django Web Framework][0]搭建的社区网站.

[![Build Status](https://travis-ci.org/lichun19960112/bootcamp.svg?branch=master)](https://travis-ci.org/lichun19960112/bootcamp)

这个项目是我刚学Python的时候关注的，以当时战五渣的水平去修改这个程序了！

在Fork原项目的基础上添加了中文国际化支持、允许游客身份访问、Feeds超级用户删除权限, 还有一些微小的改动

介于当时不熟悉Django的正确的开发姿势和GitHub的使用，(写出了屎一样的code 和 git commit message)

导致Pull requests的Comparing changes已经面目全非了，没有被merged的可能了

在我工作一段时间后，想起重新搞搞这个项目, 接下来准备修改支持Python3和最新新版本的Django 

现在用上了travis ci做持续集成, 再补上单元测试, 按正常的开发流程来，用pull requests，之前都是往master提交


## 示例
Bootcamp已经部署在SAE SC2容器环境上 [http://bootcamp.lichun.me/][1].

## 部署方式

SAE容器使用方式详情请看文档 [SAE Python应用部署指南][2].

```python
git clone git@github.com:lichun19960112/bootcamp.git 

pip install -r requirements.txt

# 根据需要修改bootcamp/settings.py配置文件
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app_' + os.environ.get('APPNAME', 'bootcamp'),
        'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
        'PORT': int(os.environ.get('MYSQL_PORT', '3306')),
        'USER': os.environ.get('ACCESSKEY', 'root'),
        'PASSWORD': os.environ.get('SECRETKEY', ''),
    }
}

python manage.py migrate
python manage.py runserver
```

[0]: https://www.djangoproject.com/
[1]: http://bootcamp.lichun.me/
[2]: http://www.sinacloud.com/doc/sae/docker/python-getting-started.html
