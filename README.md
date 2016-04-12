## Bootcamp是一个[Python Django][0]构建的社区论坛类网站.

[![Build Status](https://travis-ci.org/qulc/bootcamp.svg?branch=master)](https://travis-ci.org/qulc/bootcamp)

这个项目是我刚学Python的时候关注的, 以当时战五渣的水平去修改这个程序了. 在Fork原项目的基础上添加了中文国际化支持、允许游客身份访问、Feeds超级用户删除权限, 还有一些微小的改动.

介于当时没有掌握正确的开发姿势，(写出了屎一样的code & git commit message), 导致现在Pull requests的Comparing changes已经面目全非了，只有作者眼瞎才有可能merge的提交了

接下来就当做自己练手的项目吧，准备修改支持Python3和最新新版本的Django, 现在用上了travis ci做持续集成, 再补上单元测试, 按正常的开发流程来，用pull requests，不再直接往master提交

## 示例
Bootcamp已经部署在SAE SC2容器环境上 [http://bootcamp.lichun.me/][1].

## 部署方式

SAE容器使用方式详情请看文档 [SAE Python应用部署指南][2].

```bash
$ git clone https://github.com/qulc/bootcamp.git

$ cd bootcamp/

$ pip install -r requirements.txt

# 根据需要修改Django和uWsgi的配置文件, 现项目可直接push到SAE容器运行
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

$ python manage.py migrate

$ uwsgi bootcamp.ini
```

[0]: https://www.djangoproject.com/
[1]: http://bootcamp.lichun.me/
[2]: http://www.sinacloud.com/doc/sae/docker/python-getting-started.html
